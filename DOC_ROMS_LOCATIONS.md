# Introdução

# Como instalar as dependências do projeto:

- python -m venv venv = instala o ambiente virtual
- pip install -r requirements.txt = instala todas as dependências

# Como rodar o código localmente

- utilize o comando flask run --no-reload no terminal e a aplicação inicia
- **Importante:** como temos um agendador de tarefas a cada 1 hora ele vai buscar a agenda dos clientes e enviar o e-mail para aquele período que tiver consultas, com o flask no modo debug normal vai duplicar essa atividade, por isso o --no-reload no comand flask run

## Prefixos

Lista de prefixos utilizados nesta API:

- **nm** = nome
- **nr** = número
- **ds** = descrição
- **dt** = data
- **fl** = flag

# /rooms

Este endpoint trata de todos os registros das salas da clínica, as quais são possíveis alugar por dias ou horas. Cada Terapeuta precisa ter um sala para poder prestar serviçoes na Clínica.
Uma sala, tem a seguinte estrutura no banco de dados:

- **nm_room**: nome da sala - **string de no máximo 50 caracteres**
- **id_specialty**: id da specialty relacionada a essa sala - **numero inteiro**
- **ds_status**: status da situação da sala em relação a um locação **string de no máximo 15 caracteres**

<hr></br>

## **GET**: **_baseUrl_**/rooms

Traz a lista de salas e por padrão vem com a primeira página com 10 items.

### **_Query Params_**

Esta rota aceita os seguintes parâmetros:

- **page**: número da página, por padrão retorna a página 1;
- **per_page**: limita a quantidade de salas por página, por padrão retorna 10;
- **dir**: ordena de forma crescente ou decrescente;
- **order_by**: ordena por qualquer campo de rooms

Exemplo de url:
**\_baseUrl/rooms?order_by=nm_room&page=1&per_page=5&dir=dsc**

- nesse exemplo está sendo mostrado uma ordenação descendente pelo nome da sala, sendo retornado a primeira página de dados com 5 registros de cada vez. Pode ser usado todos os query params, ou apenas alguns ou nenhum.

```json
    response 200
[
  {
    "id_room": 4,
    "nm_room": "Sala 04",
    "ds_status": "livre",
    "specialty": {
      "id_specialty": 4,
      "nm_specialty": "Constalação Familiar"
    }
  },
  {
    "id_room": 3,
    "nm_room": "Sala 03",
    "ds_status": "livre",
    "specialty": {
      "id_specialty": 3,
      "nm_specialty": "Tarô Terapêutico"
    }
  },
  {
    "id_room": 2,
    "nm_room": "Sala 02",
    "ds_status": "livre",
    "specialty": {
      "id_specialty": 2,
      "nm_specialty": "Heiki Usui"
    }
  },
  {
    "id_room": 1,
    "nm_room": "Sala 01",
    "ds_status": "livre",
    "specialty": {
      "id_specialty": 1,
      "nm_specialty": "Astrologia"
    }
  }
]
```

<hr></br>

## **GET**: **_baseUrl_**/rooms/{id}

Retorna uma sala pelo seu id.

```json
   response 200

   {
        "id_room": 2,
        "nm_room": "Sala 02",
        "ds_status": "livre",
        "specialty": {
            "id_specialty": 2,
            "nm_specialty": "Heiki Usui"
            }
    }
```

<hr></br>

## **GET**: **_baseUrl_**/rooms/status

Retorna as salas por seus status, e a digitação do status não precisa ser por completo, se digitar apenas 'liv' já retorna os status que contém essas letras.
É possível utilizar alguns parâmetros na url para organizar melhor a busca:

### **_Query Params_**

- **dir**: alteração da direção de forma crescente ou decrescente;
- **order_by**: ordena por qualquer campo de rooms

Exemplo de url:
**\_baseUrl/rooms/liv?dir=asc&order_by=id_room**

Neste exemplo, retorna-se os dados do status 'livre', foi digitado apenas rooms/liv e ordenado por id_room de forma crescente

```json
   response 200

   [
    {
        "id_room": 1,
        "nm_room": "Sala 01",
        "ds_status": "livre",
        "specialty": {
        "id_specialty": 1,
        "nm_specialty": "Astrologia"
        }
    },
    {
        "id_room": 2,
        "nm_room": "Sala 02",
        "ds_status": "livre",
        "specialty": {
        "id_specialty": 2,
        "nm_specialty": "Heiki Usui"
        }
    },
    {
        "id_room": 3,
        "nm_room": "Sala 03",
        "ds_status": "livre",
        "specialty": {
        "id_specialty": 3,
        "nm_specialty": "Tarô Terapêutico"
        }
    },
    {
        "id_room": 4,
        "nm_room": "Sala 04",
        "ds_status": "livre",
        "specialty": {
        "id_specialty": 4,
        "nm_specialty": "Constalação Familiar"
        }
    }
]
```

<hr></br>

## **GET**: **_baseUrl_**/rooms/schedule/id_room

Retorna as consultas agendadas pelo id da sala.

### **_Query Params_**

Esta rota aceita o seguite parâmetro:

- status_consulta = retorna apenas o status informado, se não for informado retorna todos os dados.

Exemplo abaixo sem utilizar o filtro por status

```json
   response 200

[
  {
    "id_session": 16,
    "id_customer": 5,
    "id_therapist": 1,
    "dt_start": "Fri, 24 Dec 2021 13:10:00 GMT",
    "dt_end": "Wed, 22 Dec 2021 13:40:00 GMT",
    "ds_status": "concluido"
  },
  {
    "id_session": 9,
    "id_customer": 3,
    "id_therapist": 1,
    "dt_start": "Sat, 09 Jan 2021 10:20:00 GMT",
    "dt_end": "Sat, 09 Jan 2021 10:40:00 GMT",
    "ds_status": "agendado"
  },
  {
    "id_session": 10,
    "id_customer": 4,
    "id_therapist": 1,
    "dt_start": "Sun, 09 Jan 2022 11:10:00 GMT",
    "dt_end": "Sun, 09 Jan 2022 11:30:00 GMT",
    "ds_status": "agendado"
  },
  {
    "id_session": 15,
    "id_customer": 8,
    "id_therapist": 1,
    "dt_start": "Thu, 23 Dec 2021 12:50:00 GMT",
    "dt_end": "Wed, 22 Dec 2021 13:20:00 GMT",
    "ds_status": "cancelada"
  }
]
```

Exemplo de URL com filtro:
**_baseUrl_/rooms/schedule/1?status_consulta=cancelada**

```json
[
  {
    "id_session": 15,
    "id_customer": 8,
    "id_therapist": 1,
    "dt_start": "Thu, 23 Dec 2021 12:50:00 GMT",
    "dt_end": "Wed, 22 Dec 2021 13:20:00 GMT",
    "ds_status": "cancelada"
  }
]
```

<hr></br>

## **POST**: **_baseUrl_**/rooms

Cadastra uma nova sala

**Important**

- **campos obrigatórios**: 'nm_room', 'id_specialty';
- os campos não obrigatórios devem seguir o seguinte formato: `{"any_key": ""}`
- o campos de status não é obrigatório porém se não for informado, por padrão é cadastrado com o status 'ativo'

```json
    request

    {
	"nm_room": "Sala 04",
	"id_specialty":4,
	"ds_status":"livre"
    }
```

```json
   response: 201

   {
        {
        "id_room": 4,
        "nm_room": "Sala 04",
        "ds_status": "livre",
        "specialty": {
            "id_specialty": 4,
            "nm_specialty": "Constaleção Familiar"
            }
        }
    }
```

<hr></br>

## **PATCH**: **_baseUrl_**/attendants/{id}

Atualiza os dados de uma sala pelo seu id

**Important**

- **id_room** não pode ser atualizado

```json
    request:

    {
        "nm_room": "Sala One"
    }
```

```json
   response 201

   {
        "id_room": 1,
        "nm_room": "Sala One",
        "ds_status": "reservada",
        "specialty": {
            "id_specialty": 1,
            "nm_specialty": "Astrologia"
        }
    }
```

<hr></br>

## **DELETE**: **_baseUrl_**/rooms/{id}

Deleta o registro de um sala pelo seu id

Exemplo de url:
**_baseUrl/rooms/1_**

Retorna os dados deletados para uma última conferência.

```json
    response 201

    {
        "Sala Deletada": {
            "id_room": 5,
            "nm_room": "Sala 20",
            "ds_status": "ativo",
            "specialty": {
            "id_specialty": 4,
            "nm_specialty": "Constalação Familiar"
            }
        }
    }
```

<hr></br></br>

# /locations

Uma locação sempre estará atrelada a um terapeuta _(id_therapist)_, a uma clínica _(id_clinic)_ e a uma sala _(id_room)_. Sua estrutura é da seguinte forma:

- **"dt_start"**: data que se inicia a locação - **deve ser informada com data e hora** = "01/12/2022 13:40:00"

- **"dt_end"**: data que se finaliza a locação = "day60" ou "hr20"\*

- **"id_room"**: id da sala que se quer locar - **número inteiro**
- **"id_clinic"**: id da clínica onde se vai alugar a sala - **número inteiro**
- **"id_therapist"**: id do terapeuta que está fazendo a locação - **número inteiro**

## Atenção ao campo dt_end

- "hr20" : hr significa horas e o número a frente a quantidade de horas de locação. Se a locação vai durar 36 hrs, a forma de se preencher esse campo é "hr36"
- "day1" : day significa dia e o número a frente a quantidade de dias de locação. Se a locação vai durar 5 dias, a forma de preencher esse campo é "day5"
- o cálculo da data final é feito automaticamente, por tanto **NÃO PASSE** um data aqui.
<hr></br>

## **GET**: **_baseUrl_**/locations

Retorna a lista de locações

### **_Query Params_**

Esta rota aceita os seguintes parâmetros:

- **page**: número da página, por padrão retorna a página 1;
- **per_page**: limita a quantidade de locações por página, por padrão retorna 10;
- **dir**: direciona os dados de forma crescente ou decrescente;
- **order_by**: ordena por qualquer campo de locations
- **filt_por**: escolher um campo para filtrar
- **filt_valor**: escolher um valor do campo que se quer filtrar

O parâmetro _filt_por_ foi pensando para ser usado com datas, os campos 'dt_start' e 'dt_end' por exemplo, mas nada impede de ser usado por qualquer outro campo.
O parâmetro _filt_valor_ juntamente com _filt_por_ torna-se possível filtrar as locações por datas. Os dados retornam sempre da data escolhida em diante.

Exemplo de url:
**_baseUrl_/locations?filt_por=dt_start&dir=asc&order_by=dt_start&filt_valor=2021/12/08**

Filtrando pela data inicial da locação, nas datas acima de 08 de dezembro de 2021, direção ascendente, ordenado pela data inicial da locação.

### **importante**: note que no filtro a data precisa ser informada no padrão yyyy/mm/dd

\*_Se não for informado qualquer parâmetro a busca retorna todas as locações apenas_

```json
    response, 200
[
  {
    "id_location": 1,
    "dt_start": "Thu, 01 Dec 2021 13:40:00 GMT",
    "dt_end": "Mon, 30 Jan 2022 13:40:00 GMT",
    "room": {
      "nm_room": "Sala One",
      "ds_status": "reservada"
    },
    "therapists": "Rafael Bertoldo"
  },
  {
    "id_location": 3,
    "dt_start": "Tue, 20 Dec 2021 13:40:00 GMT",
    "dt_end": "Sun, 25 Dec 2022 13:40:00 GMT",
    "room": {
      "nm_room": "Sala 03",
      "ds_status": "reservada"
    },
    "therapists": "Mateus F Gava"
  },
  {
    "id_location": 2,
    "dt_start": "Mon, 26 Dec 2021 13:40:00 GMT",
    "dt_end": "Wed, 25 Jan 2022 13:40:00 GMT",
    "room": {
      "nm_room": "Sala 02",
      "ds_status": "reservada"
    },
    "therapists": "Victor Santos"
  }
]
```

<hr></br>

## **GET**: **_baseUrl_**/locations/id

Retorna uma locação pelo seu id.

```json
   response 200

   {
        "id_location": 1,
        "dt_start": "Thu, 01 Dec 2021 13:40:00 GMT",
        "dt_end": "Mon, 30 Jan 2022 13:40:00 GMT",
        "room": {
            "nm_room": "Sala One",
            "ds_status": "reservada"
        },
        "therapists": "Rafael Bertoldo"
    }
```

<hr></br>

## **GET**: **_baseUrl_**/locations/therapist/id

Retorna as locações pelo id do terapeuta

Exemplo de url:
**_baseUrl_/locations/therapist/2**
Retornou todas locações do terapeuta id 2

```json
   response 200

   [
        {
            "id_location": 4,
            "dt_start": "Tue, 20 Dec 2022 09:00:00 GMT",
            "dt_end": "Sat, 24 Dec 2022 09:00:00 GMT",
            "room": {
            "id_room": 4,
            "nm_room": "Sala 04",
            "ds_status": "reservada"
            },
            "therapists": "Rafael Leonardo"
        },
        {
            "id_location": 5,
            "dt_start": "Tue, 27 Dec 2022 09:00:00 GMT",
            "dt_end": "Mon, 27 Mar 2023 09:00:00 GMT",
            "room": {
            "id_room": 3,
            "nm_room": "Sala 03",
            "ds_status": "reservada"
            },
            "therapists": "Rafael Leonardo"
        }
    ]
```

<hr></br>

## **POST**: **_baseUrl_**/locations

Cadastra uma nova locação

**Important**

- **campos obrigatórios**: 'dt_start', 'id_room', 'id_clinic', 'id_therapist';
- os campos não obrigatórios devem seguir o seguinte formato: `{"any_key": ""}`
- é altamente recomendado que sempre seja informado uma data final de locação no campo 'dt_end'
- o status da sala informada é automaticamente atualizado para _reservada_ quando se cria uma nova locação

```json
    request

    {
        "dt_start": "26/12/2021 13:40:00",
        "dt_end": "day30",
        "id_room": 2,
        "id_clinic": 1,
        "id_therapist":3
    }
```

```json
   response: 201

   {
        "id_location": 2,
        "dt_start": "Mon, 26 Dec 2021 13:40:00 GMT",
        "dt_end": "Wed, 25 Jan 2022 13:40:00 GMT",
        "room": {
            "id_room": 2,
            "nm_room": "Sala 02",
            "ds_status": "reservada",
            "specialty": {
            "id_specialty": 2,
            "nm_specialty": "Heiki Usui"
            }
        }
    }
```

O status da sala 2 antes de criar a locação estava como livre

```json
{
  "id_room": 2,
  "nm_room": "Sala 02",
  "ds_status": "livre",
  "specialty": {
    "id_specialty": 2,
    "nm_specialty": "Heiki Usui"
  }
}
```

Após a locação ter sido concluída veja que o status agora é _reservada_

```json
{
  "id_room": 2,
  "nm_room": "Sala 02",
  "ds_status": "reservada",
  "specialty": {
    "id_specialty": 2,
    "nm_specialty": "Heiki Usui"
  }
}
```

<hr></br>

## **PATCH**: **_baseUrl_**/locations/id

Atualiza os dados de uma locação pelo seu id

**Important**

- o campo _dt_dtart_ não pode ser alterado sozinho, _dt_end_ precisa ser informado também. No entanto é possível alterar apenas _dt_end_
- Quando se altera uma locação automaticamente o status de room é alterado para _reservada_
- todos os campos são alteráveis, fora a regra das datas explicado acima

Exemplo de Url:
**_base_Url_/locations/2**

```json
    request
{

	"dt_start":"20/12/2021 10:00:00",
	"dt_end":"day30"

}
```

```json
    response 201

    {
        "id_location": 2,
        "dt_start": "Mon, 20 Dec 2021 10:00:00 GMT",
        "dt_end": "Wed, 19 Jan 2022 10:00:00 GMT",
        "room": {
            "id_room": 2,
            "nm_room": "Sala 02",
            "ds_status": "reservada",
            "specialty": {
            "id_specialty": 2,
            "nm_specialty": "Heiki Usui"
            }
        }
    }
```

## **PATCH**: **_baseUrl_**/locations/id

Deleta um registro de locação

**Importante**: ao se excluir um registro de locação, o status da sala atrelado ao processo atualiza para o status "livre"

Exemplo de Url:
**_base_Url_/locations/11**

Retorna os dados excluídos para uma última conferência

```json
{
  "Locação Excluída": {
    "id_location": 11,
    "dt_start": "Fri, 09 Dec 2022 18:40:00 GMT",
    "dt_end": "Sat, 24 Dec 2022 18:40:00 GMT",
    "room": {
      "id_room": 2,
      "nm_room": "Sala Tunel Do Tempo",
      "ds_status": "livre",
      "specialty": {
        "id_specialty": 4,
        "nm_specialty": "Constalação Familiar"
      }
    }
  }
}
```
