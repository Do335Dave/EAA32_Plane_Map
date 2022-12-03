function selected_planes() {
    let str_planes = "";
    let collection = document.getElementsByName("plane_check");
    for (let p = 0; p < collection.length; p++) {
      if (collection[p].checked) {
        str_planes += collection[p].value;
      }
    }
    alert(str_planes);
 }