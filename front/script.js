let url = 'http://127.0.0.1:8000/';

function enviarDado(){
    let userName = document.querySelector('#userName').value;
    let data = {
        user_name: userName
    }

    fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data), })
        .then(response => response.json())
        .then(data => { console.log('Resposta da API:', data); })
        .catch(error => { console.error('Erro:', error);
    });
}

function carregarRecomendations(){
    fetch(url, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' }})
        .then(response => response.json())
        .then(data => {
            console.log('Resposta da API:', data.recomendations);
            const recomendations = data.recomendations;
            recomendations.map((item) => {
                let card = document.querySelector('.card').cloneNode(true);
                let areaRecomendations = document.querySelector('.areaRecomendations');
                let nomeFilme = item[1];
                let porcentagem = (item[0] * 100)/5;
                card.querySelector('.title-filme').innerHTML = nomeFilme;
                card.querySelector('#porcentagemFilme').innerHTML = `${porcentagem.toFixed(1)}%`;
                areaRecomendations.append(card)
            })
        })
        .catch(error => { console.error('Erro:', error);
    });
}