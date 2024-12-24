const mykeys = window.location.href.split('?')[1].split('&');
const resource_id = mykeys[0].split('=')[1];
const filters = mykeys[1].split('=')[1];
// Replace these placeholders with actual values
const apiUrl = `https://data.gov.il/api/3/action/datastore_search?resource_id=${resource_id}&filters=${filters}`;

async function makeApiRequest(method = 'GET') {
    const headers = {
    };

    const requestOptions = {
        method,
        headers,
    };

    const response = await fetch(apiUrl, requestOptions);
    const responseData = await response.json();
    return responseData;
}


const response = makeApiRequest(method = 'GET').then(data => {

    console.log(data.result.records[0]);
    value = data.result.records[0];

    const table = document.getElementById('energyTable');
    //delet _id field from the object

    let first = true;

    Object.entries(value).forEach(item => {
      if (first) {
        first = false;
        return;
      }
        const row = table.insertRow();
        const valueCell = row.insertCell(0);
        const CategoryCell = row.insertCell(1);

        CategoryCell.textContent = item[0];
        valueCell.textContent = item[1];
      });
  })
  .catch(error => {
    console.error('Error fetching JSON:', error);
  });