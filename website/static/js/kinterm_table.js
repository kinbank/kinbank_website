function fill_table(data, table_class){
    var table = new Tabulator(table_class, {
        height:200, // set height of table to enable virtual DOM
        data:data, //load initial data into table
        layout:"fitColumns", //fit columns to width of table (optional)
        columns:[ //Define Table Columns
            {title:"Parameter", field:"Parameter", sorter:"string"},
            {title:"Male speaker", field:"m", sorter:"string"},
            {title:"Female speaker", field:"f", sorter:"string"}
        ]
    });

}

(function() {
    $(document).ready(function() {
      $('.switch-input').on('change', function() {
        var isChecked = $(this).is(':checked');
        var selectedData;
        var $switchLabel = $('.switch-label');
        console.log('isChecked: ' + isChecked); 
  
        if(isChecked) {
          selectedData = $switchLabel.attr('data-on');
        } else {
          selectedData = $switchLabel.attr('data-off');
        }
  
        console.log('Selected data: ' + selectedData);
  
      });
    });
  
  })();