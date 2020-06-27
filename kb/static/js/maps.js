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
	
	console.log(markers[1])
	for ( var i=0; i < markers.length; ++i ) 
	{

	   L.circle( [markers[i].lat, markers[i].long] , {color: '#ED5C4D', opacity:.5})
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

	map.on('zoomend', function(e) {
	    myZoom.end = map.getZoom();
	    var diff = myZoom.start - myZoom.end;
	    if (diff > 0) {
	        circle.setRadius(circle.getRadius() * 2);
	    } else if (diff < 0) {
	        circle.setRadius(circle.getRadius() / 2);
	    }
	});

}