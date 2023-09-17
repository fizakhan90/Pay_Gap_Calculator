document.addEventListener('DOMContentLoaded', function(){

    const getData = document.getElementById('getData');
    const resultParagraph = document.getElementById('result');

    getData.addEventListener('click', function(){
        fetch('/get_mean_salary')
        .then(response => response.json())
            .then(data => {
              resultParagraph.textContent = 'Mean Salary: ' + data.mean_salary;
            })
            .catch(error => {
                console.error('Error:', error);
            });
    })
})