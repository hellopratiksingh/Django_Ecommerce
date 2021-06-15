var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var cycleId = this.dataset.cycle
        var action = this.dataset.action
        console.log('cycleId:', cycleId, 'Action:', action)
        console.log('USER:', user)

        if (user == 'AnonymousUser') {
            addCookieItem(cycleId, action)
        } else {
            updateUserOrder(cycleId, action)
        }
    })
}

function updateUserOrder(cycleId, action) {
    console.log('User is authenticated, sending data...')

    var url = 'update_item'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'cycleId': cycleId, 'action': action })
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
        });
}