// const { default: axios } = require("axios")
const BASE_URL = 'http://localhost:5000/api'

function generateCupcakes(cupcake) {
    return $(`<div cupcake-data-id=${cupcake.id}> 
       <li>${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}</li>
       <img class="cupcake-image" src="${cupcake.image}" alt="(No Image Provided)" width=100 height = 100>
       </div>`)
}

async function getInitialCupcakes() {
    const response = await axios.get('http://127.0.0.1:5000/api/cupcakes');
    console.log(response)
    for (let cupcakeData of response.data.data) {
        let newCupcake = generateCupcakes(cupcakeData);
        $('#cupcakes-list').append(newCupcake)
        console.log(cupcakeData);
    }

}

$('#new-cupcake').on('submit', async function(evt){
    evt.preventDefault()

    let flavor = $('#form-flavor').val()
    let size = $('#form-size').val()
    let rating = $('#form-rating').val()
    let image = $('#form-image').val()

    const newCupcakeRequest = await axios.post(`api/cupcakes`, 
        {
            flavor,
            size,
            rating,
            image 
        })
        let newCupcake = $(generateCupcakes(newCupcakeRequest.data.data));
    $("#cupcakes-list").append(newCupcake);
    $("#new-cupcake-form").trigger("reset");
    });

getInitialCupcakes()

    

