function fill_diagram(terms, diagram='kinshipdiagram'){
    var svgDocument
    svgObject = document.getElementById(diagram);
    svgDocument = svgObject.contentDocument;

    for (var i = 0; i < terms.length; i++){
        if(terms[i].parameter_id == null) // this skips over the language name change
            continue;

        var kincode = terms[i].parameter_id 
        text = svgDocument.getElementById(kincode)
        if (text != null){
            text.textContent = terms[i].form;
            text.style.fontSize = "20px"
            text.style.font = "sans-serif"
        }

        shape = svgDocument.getElementById(kincode + "Shape")

        if (shape != null && kincode != null){
            shape.style.fill = terms[i].colour;
           
            // trying to get mouse over for extr terms here
            // if(terms[i].extra != null){
            //     shape.addEventListener('click', function() {
            //         svgDocument.getElementById("mM").style.fill = "#57B5ED";
            //     })
            // }
        }
    }

    //  mouse over example code
    svgDocument.getElementById("mMShape")
          .addEventListener('click', function(e) {
          e.currentTarget.setAttribute('fill', '#ff00cc');
        });



    language_name = svgDocument.getElementById('language_name')
    if(language_name != null){
        language_name.textContent = terms[6].language_name
        language_name.style.fontSize = "25px"
        language_name.style('fill', "#57B5ED") 
    }
    
    // change sex of speaker caoption 
    // speaker_text = parameter.substr(parameter.length - 2);
    // speaker_obj = svgDocument.getElementById("speaker");
    // if (speaker_text != null){
    //         speaker_obj.textContent = speaker_text;
    //         speaker_obj.style.fontSize = "20px"
    // }
}