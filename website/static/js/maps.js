function main(markers){

	var map = L.map( 'map', {
	    center: [20.0, 5.0],
	    minZoom: 2,
	    zoom: 2
	});

	L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
	    subdomains: ['a','b','c']
	}).addTo( map );

	for ( var i=0; i < markers.length; ++i ) {
	   L.circleMarker( [markers[i].lat, markers[i].long] , {color: '#ED5C4D', opacity:.5, radius: 5})
	      .bindPopup( '<a href="' + markers[i].glottocode + '" ">' + markers[i].culture + '</a>' )
	      .addTo( map );
	}

	var myZoom = {
	  start:  map.getZoom(),
	  end: map.getZoom()
	};

	map.on('zoomstart', function(e) {
	   myZoom.start = map.getZoom();
	});

}

function detail_map(lat, lon){

	var map = L.map("map_detail", {
	    center: [lat, lon],
	    minZoom: 2,
	    zoom: 3,
	    zoomControl: false,
	});

	L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
	    subdomains: ['a','b','c']
	}).addTo( map );
	
	L.circle( [lat, lon] , 200000, {color: '#ED5C4D', fillColor: '#ED5C4D', fillOpacity : 0.7})
	      .addTo( map );
}


