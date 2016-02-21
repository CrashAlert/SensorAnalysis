import fetch from 'isomorphic-fetch'
import $ from 'jquery'

const url = '/store'
const linkBaseUrl = '/map.html?fileName='

window.loadRides = function loadRides() {
  fetch(url)
    .then(response => response.json())
    .then(addRidesToList)
}

function addRidesToList(rideNames) {
  const elems = rideNames.map(createListElem)
  $('#rides > ul').append(elems)
}

function createListElem(name) {
  return $("<li>").append($("<a>")
      .text(name)
      .attr('href', linkBaseUrl + name)
    )
}
