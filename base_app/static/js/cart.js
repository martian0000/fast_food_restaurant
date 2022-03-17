var updateBtns = document.getElementsByClassName('update-cart')


for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var mealId = this.dataset.meal
        var action = this.dataset.action
        console.log('mealId:', mealId, 'action:', action)

        console.log('USER:', user)
        if(user === 'AnonymousUser' ){
            console.log('Not logged in')

        }else{
            updateUserOrder(mealId, action)
        }

    })

}

function updateUserOrder(mealId, action){
    console.log('User is logged in, sending data ..')

    var url = '/update_item/'
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'mealId': mealId, 'action': action})
    })

    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}