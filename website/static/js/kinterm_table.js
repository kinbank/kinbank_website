function fill_table(data){
    var table = new Tabulator("#example-table", {
        height:200, // set height of table to enable virtual DOM
        data:data, //load initial data into table
        layout:"fitColumns", //fit columns to width of table (optional)
        columns:[ //Define Table Columns
            {title:"Parameter", field:"Parameter", sorter:"string"},
            {title:"Female speaker", field:"f", sorter:"string"},
            {title:"Male speaker", field:"m", sorter:"string"},
        ]
    });

}

