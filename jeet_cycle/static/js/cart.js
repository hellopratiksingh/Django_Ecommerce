var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var cycleId = this.dataset.cycle;
        var action = this.dataset.action;
        console.log('cycleId:', cycleId, 'action:', action)

        console.log('USER:', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            console.log('user is logged in, sending data')
        }
    })
}
 

function updateUserOrder(cycleId, action) {
    console.log('User is Logged in, sending data... ');
    
    var url = '/update_item'

    fetch(url, {
        method:'POST',
        headers:{
            'content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'cycleId': cycleId, 'action':action})
    })

    .then((response) =>{
        return response.json();
    })
    .then((data) => {
        console.log('data:', data)
    })
}

