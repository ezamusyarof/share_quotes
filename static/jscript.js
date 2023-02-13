function like(id){
    document.getElementById('like-btn-wh-'+id).style.display = 'none';
    document.getElementById('like-btn-red-'+id).style.display = 'block';
    document.getElementById('q-'+id).innerHTML = parseInt((document.getElementById('q-'+id).innerHTML))+1
    minAjax({
        url:"http://127.0.0.1:2000/like/"+id,
        type:"POST",
        data:{}
    });
}

function dislike(id){
    document.getElementById('like-btn-wh-'+id).style.display = 'block';
    document.getElementById('like-btn-red-'+id).style.display = 'none';
    document.getElementById('q-'+id).innerHTML = parseInt((document.getElementById('q-'+id).innerHTML))-1
    minAjax({
        url:"http://127.0.0.1:2000/dislike/"+id,
        type:"POST",
        data:{}
    });
}

function openForm(){
    document.getElementById('box-form-open').style.display = 'block';
    }
    function closeForm(){
    document.getElementById('box-form-open').style.display = 'none';
    }
    function sendQuote(){
    document.getElementById('box-form-open').style.display = 'none';
    var quote = document.getElementById('quote-text-input').value
    var name = document.getElementById('your-name-input').value
    minAjax({
        url:"http://127.0.0.1:2000/add_quote",
        type:"POST",
        data:{
            your_name:name,
            quote_text:quote,
        },
        success: function(data){
            alert(data);
        }
    });
    window.location.reload();
}

function load_data(){
    let response = fetch("http://127.0.0.1:2000/api_quote",{    
        method: 'GET',    
        withCredentials: true,    
        crossorigin: true,    
        mode: 'no-cors',
    })
    response
    .then( res => {
        console.log(res.text());
        return res.text();
    })
        .then( json => {
        console.log(json);
    });
}