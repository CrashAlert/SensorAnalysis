import fetch from 'isomorphic-fetch'
import _ from 'lodash'

const baseUrl = "/map/"

var map;

var waypoints = [
    {lat: 37.772, lng: -122.214},
    {lat: 21.291, lng: -157.821},
    {lat: -18.142, lng: 178.431},
    {lat: -27.467, lng: 153.027}
  ];

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 3,
    center: {lat: -180, lng: -180},
  })

  // handleData(waypoints)

  fetchDataPoints()
    .then(response => response.json())
    .then(handleData)
}

window.initMap = initMap


// http://stackoverflow.com/questions/901115/how-can-i-get-query-string-values-in-javascript
function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

function fetchDataPoints() {
  const url = baseUrl + getParameterByName("fileName")
  return fetch(url)
}

function maxError(elem) {
  return _.max([elem.err_lat, elem.err_lng])
}

function handleData(rawData) {
  let data
  if (getParameterByName('filterData') != '') {
    let filterVal = parseInt(getParameterByName('filterData'))
    data = _.filter(rawData, elem => {
      return maxError(elem) < filterVal
    })
  } else {
    data = rawData
  }

  let waypoints = _.map(data, (elem) => _.pick(elem, ['lat', 'lng']))

  addLines(waypoints)
  addMarkers(waypoints)
  fitWaypoints(waypoints)
  if (getParameterByName('showErrors') == '1') {
    addErrors(data)
  }
}

function fitWaypoints(waypoints) {
  const bounds = waypoints.reduce((bounds, waypoint) => {
      const pos = new google.maps.LatLng(waypoint.lat, waypoint.lng)
      return bounds.extend(pos)
    }, new google.maps.LatLngBounds())
  map.setCenter(bounds.getCenter())
  map.fitBounds(bounds)
}

function addErrors(data) {
  _.forEach(data, elem => {
    let location = _.pick(elem, ['lat', 'lng'])
    let error = maxError(elem)
    new google.maps.Circle({
      strokeColor: '#FF0000',
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: '#FF0000',
      fillOpacity: 0.1,
      map: map,
      center: location,
      radius: error
    })
  })
}

function addMarkers(waypoints) {

  const circle = {
    fillColor: "CC0000",
    strokeColor: "CC0000",
    path: google.maps.SymbolPath.CIRCLE,
    scale: 3,
    strokeWeight: 1
  }

  for (let waypoint of waypoints) {
    new google.maps.Marker({
      position: waypoint,
      map: map,
      icon: circle
    })
  }
}

function addLines(waypoints) {
  const path = new google.maps.Polyline({
    path: waypoints,
    strokeColor: '#FF0000',
    strokeOpacity: 1.0,
    strokeWeight: 2
  })

  path.setMap(map)
}
