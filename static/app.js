// const { default: axios } = require("axios")

$('#new-cupcake').click(async function(evt){
    evt.preventDefault()

    let flavor = $('#flavor').val()
    let size = $('#size').val()
    let rating = $('#rating').val()
    let image = $('#image').val()

    const newCupcakeRequest = await axios.post('/api/cupcakes', 
        {
            flavor,
            size,
            rating,
            image 
        })
    });

