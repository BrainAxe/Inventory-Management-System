async function fetchData() {
    let response = await fetch('http://127.0.0.1:8000/api/inventory');

    if (response.status === 200) {
        let data = await response.json();
        console.log(data);
        var text = "<table> <th>Name</th> <th>Availability</th><th>Supplier</th>";
        for(let item in data){
           text+= "<tr><td>"+ "<a href='inventory/" + JSON.stringify(data[item].id) + "'>" + JSON.stringify(data[item].name)  + "</a>" +"</td><td>"+JSON.stringify(data[item].availability)+"</td><td>"+JSON.stringify(data[item].supplier_name)+"</td></tr>";
        }
        text+= "</table>"
        document.getElementById("inventory-data").innerHTML += text;
    }
}

fetchData();
