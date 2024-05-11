from flask import Flask, render_template_string
import json

app = Flask(__name__)

# Rota principal que exibe a tabela
@app.route('/')
def index():
    # Carrega os dados do arquivo JSON
    with open('dados/dados.json', 'r') as file:
        data = json.load(file)

    # Processa os dados para uma lista plana de eventos
    eventos = []
    for grupo_eventos in data:
        for evento in grupo_eventos:
            eventos.append(evento)

    # Cria uma string de template HTML
    html = '''
    
    <!DOCTYPE html>
    <html>
    <head>
        <title>Security Events</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <style>
    *{
    box-sizing: border-box;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
}
body{
    font-family: Helvetica;
    -webkit-font-smoothing: antialiased;
    background: rgba( 71, 147, 227, 1);
}
h2{
    text-align: center;
    font-size: 18px;
    
    letter-spacing: 1px;
    color: white;
    padding: 30px 0;
}

/* Table Styles */

.table-wrapper{
    margin: 10px 70px 70px;
    box-shadow: 0px 35px 50px rgba( 0, 0, 0, 0.2 );
}

.fl-table {
    border-radius: 5px;
    font-size: 12px;
    font-weight: normal;
    border: none;
    border-collapse: collapse;
    width: 100%;
    max-width: 100%;
    //white-space: nowrap;
    background-color: white;
}

.fl-table td, .fl-table th {
    text-align: center;
    padding: 8px;
}

.fl-table td {
    border-right: 1px solid #f8f8f8;
    font-size: 12px;
}

.fl-table thead th {
    color: #ffffff;
    background: #4FC3A1;
}


.fl-table thead th:nth-child(odd) {
    color: #ffffff;
    background: #324960;
}

.fl-table tr:nth-child(even) {
    background: #F8F8F8;
}

/* Responsive */

@media (max-width: 767px) {
    .fl-table {
        display: block;
        width: 100%;
    }
    .table-wrapper:before{
        content: "Scroll horizontally >";
        display: block;
        text-align: right;
        font-size: 11px;
        color: white;
        padding: 0 0 10px;
    }
    .fl-table thead, .fl-table tbody, .fl-table thead th {
        display: block;
    }
    .fl-table thead th:last-child{
        border-bottom: none;
    }
    .fl-table thead {
        float: left;
    }
    .fl-table tbody {
        width: auto;
        position: relative;
        overflow-x: auto;
    }
    .fl-table td, .fl-table th {
        padding: 20px .625em .625em .625em;
        height: 60px;
        vertical-align: middle;
        box-sizing: border-box;
        overflow-x: hidden;
        overflow-y: auto;
        width: 120px;
        font-size: 13px;
        text-overflow: ellipsis;
    }
    .fl-table thead th {
        text-align: left;
        border-bottom: 1px solid #f7f7f9;
    }
    .fl-table tbody tr {
        display: table-cell;
    }
    .fl-table tbody tr:nth-child(odd) {
        background: none;
    }
    .fl-table tr:nth-child(even) {
        background: transparent;
    }
    .fl-table tr td:nth-child(odd) {
        background: #F8F8F8;
        border-right: 1px solid #E6E4E4;
    }
    .fl-table tr td:nth-child(even) {
        border-right: 1px solid #E6E4E4;
    }
    .fl-table tbody td {
        display: block;
        text-align: center;
    }
}
  </style>
            <script>
                setTimeout(function() {
                    location.reload();
                }, 10000);
            </script>
    </head>
    <body>
        <h2>AI-NetGuard</h2>
        <div class="table-wrapper">
            <table class="fl-table">
            <thead>
            <tr>
                <th>DATA_TIME</th>
                <th>Ação</th>
                <th>IP do Atacante</th>
                <th>Servidor atacado</th>
                <th style="width:45%">Descrição do ataque</th>
           </tr>
        </thead>
        <tbody>
        
                 {% for event in eventos %}
            <tr>
                <td>{{ event['DATA_TIME'] }} </td>
                <td>{{ event['ACAO'] }}</td>
                <td>{{ event['ATACANTE'] }} </td>
                <td>{{ event['IP_HOSTNAME'] }}</td>
                <td style="width:45%">{{ event['TIPO_ATAQUE'] }} </td>
            </tr>
        {% endfor %}
         <tbody>
        </table>
        </div>
    </body>
    </html>
    '''
    
        
        
    
    
          
            
    
    
    
    return render_template_string(html, eventos=eventos)

if __name__ == '__main__':
    app.run(debug=True)