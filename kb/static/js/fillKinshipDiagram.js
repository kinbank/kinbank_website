function main(terms){
    var svgDocument
    svgObject = document.getElementById('kinshipdiagram');
    svgDocument = svgObject.contentDocument;

    for (var i = 0; i < terms.length; i++){
        var kincode = terms[i].parameter_id
        var parameter = kincode
        // kincode = parameter.slice(0, -3)
        console.log(kincode)
        // text = svgDocument.getElementById(kincode + "text")
        text = svgDocument.getElementById(kincode)
        if (text != null){
            text.textContent = terms[i].form;
            text.style.fontSize = "20px"
            text.style.font = "sans-serif"
        }

        // shape = svgDocument.getElementById(kincode + "Shape")
        // if (shape != null)
        //     shape.style.fill = terms[i].colour;
    }
    
    language_name = svgDocument.getElementById('language_name')
    language_name.textContent = terms[6].language_name
    language_name.style.fontSize = "25px"
    language_name.style('fill', "#57B5ED") 

    // change sex of speaker caoption 
    // speaker_text = parameter.substr(parameter.length - 2);
    // speaker_obj = svgDocument.getElementById("speaker");
    // if (speaker_text != null){
    //         speaker_obj.textContent = speaker_text;
    //         speaker_obj.style.fontSize = "20px"
    // }
}