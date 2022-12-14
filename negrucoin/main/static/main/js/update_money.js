
function update_money() {
    $.ajax({
        url: '/api/get-money-count',
        method: 'get',
        dataType: 'json',
        success: function(data){
            $('.user__money').html(data.money)
        }
    })
}


$(document).ready(function() {
    setInterval(update_money, 10000)
})
