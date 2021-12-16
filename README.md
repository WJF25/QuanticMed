# Quantic Med

Aplicação direcionada para o gerenciamento de uma clínica de terapias holísticas.

## Introdução

Esta é uma API feita para estudo que visa atender as necessidades de uma clínica de terapidas holísticas, a qual funciona sem qualquer método de controle. A api se baseia no padrão REST. As rotas tem proteção que se baseia na autenticação do usuário, podendo o usuário ter uma flag de um terapeuta ou um atendente.

<br><hr><br>

# Como instalar as dependências do projeto:

- python -m venv venv = instala o ambiente virtual
- pip install -r requirements.txt = instala todas as dependências

<br><hr><br>

# Como rodar o código localmente

- utilize o comando flask run --no-reload no terminal e a aplicação inicia
- **Importante:** como temos um agendador de tarefas a cada 1 hora ele vai buscar a agenda dos clientes e enviar o e-mail para aquele período que tiver consultas, com o flask no modo debug normal vai duplicar essa atividade, por isso o --no-reload no comand flask run

<br><hr><br>

# Termos de Uso

Não há restrições para utilização da API. Esta API não tem fins lucrativos.

## Prefixos

Algum prefixos foram utilizados no nome da chave para facilitar a identificação de uma chave.

- **nm**: nome
- **nr**: número
- **id**: identificador
- **ds**: descrição ou comentário
- **dt**: data ou datetime
- **fl**: flag

<br><hr><br>

## /attendants

Um 'attendant' é um atendente ou recepcionista que tem acesso ao uso da platorma e tem como principal responsabilidade agendar as sessões

- **nm_attendant**: nome completo do colaborador/recepcionista
- **nr_cpf**: número do documento, deve ser uma string com 11 caracteres.
- **nr_telephone**: número de telefone residencial, string com 10 caracteres - DDD + número
- **nr_cellphone**: número de telefone móvel, string com 10 ou 11 - DDD + número
- **ds_email**: endereço de e-mail
- **ds_password**: senha para acesso
- **dt_creation_time**: data da criação do recepcionista;
- **id_clinic**: id(inteiro) da clínica onde o colaborador atua

<br><hr><br>

**GET**: **_baseUrl_**/attendants

Traz a lista de todos atendentes.

```json
    response 200
    [
        {
            "id_attendant": 2,
            "nm_attendant": "Jane Doe",
            "nr_cpf": "11122233300",
            "nr_telephone": "9933334321",
            "nr_cellphone": "9999999876",
            "ds_password": "654321",
            "ds_email": "janedoe@email.com",
            "dt_creation_time": "Thu, 09 Dec 2021 09:17:59 GMT",
            "id_clinic": 1
        },
        {
            "id_attendant": 1,
            "nm_attendant": "John Doe",
            "nr_cpf": "12345678901",
            "nr_telephone": "9933331234",
            "nr_cellphone": "9999996789",
            "ds_password": "123456",
            "ds_email": "johndoe@email.com",
            "dt_creation_time": "Thu, 09 Dec 2021 09:17:59 GMT",
            "id_clinic": 1
        }
    ]
```

<br><hr><br>

**GET**: **_baseUrl_**/attendants/{id}

Retorna um recepcionista pelo seu id

```json
   response 200

    {
        "id_attendant": 1,
        "nm_attendant": "John Doe",
        "nr_cpf": "12345678900",
        "nr_telephone": "9933331234",
        "nr_cellphone": "9999996789",
        "ds_email": "johndoe@email.com",
        "ds_password": "123456",
        "dt_creation_time": "Thu, 09 Dec 2021 09:17:59 GMT",
        "id_clinic": 1
    }
```

<br><hr><br>

**POST**: **_baseUrl_**/attendants

Cadastra um novo atendente

**Important**

- **nr_cpf** e **ds_email**deve ser único para cada atendente;

```json
    request

    {
        "nm_attendant":"John Doe",
        "nr_cpf": "12345678900",
        "nr_telephone": "9933331234",
        "nr_cellphone": "9999996789",
        "ds_email":"johndoe@email.com",
        "ds_password":"123456",
        "id_clinic":1
    }
```

```json
   response: 201

   {
        "id_attendant": 1,
        "nm_attendant": "John Doe",
        "nr_cpf": "12345678900",
        "nr_telephone": "9933331234",
        "nr_cellphone": "9999996789",
        "ds_email": "johndoe@email.com",
        "ds_password": "123456",
        "dt_creation_time": "Thu, 09 Dec 2021 09:17:59 GMT",
        "id_clinic": 1
    }
```

<br><hr><br>

**PATCH**: **_baseUrl_**/attendants/{id}

Atualiza os dados de um atendente pelo seu id

**Important**

- **id_attendant** e **id_clinic** não podem ser atualizados

```json
    request:

    {
        "ds_email":"newemail@email.com",
    }
```

```json
   response 200

   {
        "id_attendant": 1,
        "nm_attendant": "John Doe",
        "nr_cpf": "12345678900",
        "nr_telephone": "9933331234",
        "nr_cellphone": "9999996789",
        "ds_email": "newemail@email.com",
        "ds_password": "123456",
        "dt_creation_time": "Thu, 09 Dec 2021 09:17:59 GMT",
        "id_clinic": 1
    }
```

<br><hr><br>

**DELETE**: **_baseUrl_**/attendants/{id}

Deleta os dados de um recepcionista pelo seu id

```json
    response 204

    No body returned for response
```

<br><hr><br>

## /clinics

Uma 'clinic' é uma clinica em que trabalham atendentes e tem locações de sala

- **nm_clinic**: nome da clínica
- **nr_cnpj**: número do cnpj (apenas números)
- **ds_address**: endereço da clínica
- **nr_adress**: número do endereço
- **ds_complement**: complemento do endereço
- **nr_zipcode**: CEP;
- **ds_uf**: Estado;
- **ds_city**: Cidade;
- **ds_district**: distrito ou bairro
- **ds_email**: email organizacional da clinica;
- **nr_telephone**: número de telefone;
- **nr_cellphone**: número de celular de 10 a 11 dígitos

<br><hr><br>

**GET**: **_baseUrl_**/clinics

Traz a lista de todas as clincas.

```json
    response 200
    [
    {
        "id_clinic": 1,
        "nm_clinic": "QantMed",
        "nr_cnpj": "123456789876543",
        "ds_address": "R. de schrödinger",
        "nr_adress": 40,
        "ds_complement": "Tudo é relativo",
        "ds_district": "Butantan",
        "nr_zipcode": "29070180",
        "ds_city": "São Paulo",
        "ds_uf": "ES",
        "ds_email": "qantmed@hotmail",
        "nr_telephone": "993333111",
        "nr_cellphone": "9999991234"
    },
    {
        "id_clinic": 2,
        "nm_clinic": "clinca2",
        "nr_cnpj": "12123123/000113",
        "ds_address": "rua 2",
        "nr_adress": "456",
        "ds_complement": "sala 1",
        "ds_district": "protásio alves",
        "nr_zipcode": "13123-123",
        "ds_city": "porto alegre",
        "ds_uf": "RS",
        "ds_email": "clinica2@mail.com",
        "nr_telephone": "5112341234",
        "nr_cellphone": "51912341234"
    },
    {
        "id_clinic": 3,
        "nm_clinic": "clinca3",
        "nr_cnpj": "12123123/000113",
        "ds_address": "rua 3",
        "nr_adress": "789",
        "ds_complement": "sala 3",
        "ds_district": "moinho de ventos",
        "nr_zipcode": "13123-123",
        "ds_city": "porto alegre",
        "ds_uf": "RS",
        "ds_email": "clinica1@mail.com",
        "nr_telephone": "5112341234",
        "nr_cellphone": "51912341234"
    }
    ]
```

<br><hr><br>

**GET**: **_baseUrl_**/clinics/{id}

Retorna um clinica pelo seu id

```json
{
  "id_clinic": 1,
  "nm_clinic": "QantMed",
  "nr_cnpj": "123456789876543",
  "ds_address": "R. de schrödinger",
  "nr_adress": 40,
  "ds_complement": "Tudo é relativo",
  "ds_district": "Butantan",
  "nr_zipcode": "29070180",
  "ds_city": "São Paulo",
  "ds_uf": "ES",
  "ds_email": "qantmed@hotmail",
  "nr_telephone": "9933331111",
  "nr_cellphone": "9999991234"
}
```

<br><hr><br>

**POST**: **_baseUrl_**/clinics

Cadastra uma nova clinica

**Important**

- **nr_cnpj** e **ds_email** deve ser único para cada clínica;

```json
    request

    {
        "nm_clinic": "QantMed",
        "nr_cnpj": "123456789876543",
        "ds_address": "R. de schrödinger",
        "nr_adress": "40",
        "ds_complement": "Tudo é relativo",
        "ds_district": "Butantan",
        "nr_zipcode": "29070180",
        "ds_city": "São Paulo",
        "ds_uf": "ES",
        "ds_email": "qantmed@hotmail",
        "nr_telephone": "9933331111",
        "nr_cellphone": "9999991234"
    }
```

```json
   response: 201
    {
        "id_clinic": 2,
        "nm_clinic": "QantMed",
        "nr_cnpj": "123456789876543",
        "ds_address": "R. de schrödinger",
        "nr_adress": "40",
        "ds_complement": "Tudo é relativo",
        "ds_district": "Butantan",
        "nr_zipcode": "29070180",
        "ds_city": "São Paulo",
        "ds_uf": "ES",
        "ds_email": "qantmed@hotmail",
        "nr_telephone": "9933331111",
        "nr_cellphone": "9999991234"
    }
```

<br><hr><br>

**PATCH**: **_baseUrl_**/clinics/{id}

Atualiza os dados de uma clínica pelo seu id

**Important**

- **id_clinic** não podem ser atualizado

```json
    request:

    {
        "ds_uf": "SP"
    }
```

```json
   response 200

{
  "id_clinic": 1,
  "nm_clinic": "QantMed",
  "nr_cnpj": "123456789876543",
  "ds_address": "R. de schrödinger",
  "nr_address": "40",
  "ds_complement": "Tudo é relativo",
  "ds_district": "Butantan",
  "nr_zipcode": "29070180",
  "ds_city": "São Paulo",
  "ds_uf": "SP",
  "ds_email": "qantmed@hotmail",
  "nr_telephone": "9933331111",
  "nr_cellphone": "9999991234"
}
```

<br><hr><br>

**DELETE**: **_baseUrl_**/clinics/{id}

Deleta os dados de uma clinica pelo seu id

```json
    response 204

    No body returned for response
```

<br><hr><br>

## /customers

Um 'customer' é o cliente que chegou na clínica e está querendo marcar uma sessão, ele é cadastrado por um atendente

- **nm_customer**: nome do cliente, no máximo 50 caracteres
- **nr_cpf**: número do cpf do cliente, deve ser uma string com 11 caracteres.
- **nr_rg**: número do RG do cliente, deve ter de 6 a 15 caracteres
- **nm_mother**: nome da mãe
- **nm_father**: nome do pai
- **nr_healthcare**: número da carteira do convênio, máximo 30 caracteres;
- **ds_address**: endereço do cliente
- **nr_address**: númerodo endereço
- **nr_zipcode**: CEP
- **nr_telefone**: telefone do cliente
- **nr_cellphone**: celular do cliente, 10 a 11 números
- **ds_email**: e-mail do cliente
- **dt_birthdate**: Data de nascimento

<br><hr><br>

**GET**: **_baseUrl_**/customers

Traz a lista de todos os clientes.

**_Query Params_**

Esta rota aceita os seguintes parâmetros:

- **name**: consulta por nome de um cliente;

```json
    response 200
    [
    {
        "id_customer":1,
        "nm_customer": "Roberto",
        "nr_cpf":"12545696585",
        "nr_rg":"36536548659",
        "nm_mother":"Maria",
        "nm_father":"João",
        "nr_healthcare":"2351254",
        "ds_address":"gaspar dutra",
        "nr_adress": "40",
        "nr_zipcode": "88644224581",
        "nr_telephone":"01989004591",
        "nr_cellphone":"0136558125",
        "ds_email":"roberto@mail.com",
        "dt_birthdate":"03/03/1995"
    },
    {
        "id_customer":2,
        "nm_customer": "Alexandra",
        "nr_cpf":"23521245842",
        "nr_rg":"13125453210",
        "nm_mother":"Elena",
        "nm_father":"Rafael",
        "nr_healthcare":"212352425",
        "ds_address":"rua das flores",
        "nr_zipcode": "88644224321",
        "nr_adress": "100",
        "nr_telephone":"01989004591",
        "nr_cellphone":"0136558125",
        "ds_email":"alexandra@mail.com",
        "dt_birthdate":"01/25/1998"
    },
    {
        "id_customer":3,
    "nm_customer": "Amelia",
        "nr_cpf":"87521245842",
        "nr_rg":"16425453210",
        "nm_mother":"Emilia",
        "nm_father":"Sebastian",
        "nr_healthcare":"4305130",
        "ds_address":"rua das camelias",
        "nr_zipcode": "88644324321",
        "nr_adress": "69",
        "nr_telephone":"01989007691",
        "nr_cellphone":"0136554325",
        "ds_email":"amelia@mail.com",
        "dt_birthdate":"09/12/1999"
    }
    ]
```

<br><hr><br>

**GET**: **_baseUrl_**/customers/{id}

Retorna um cliente pelo seu id

```json
   response 200

{
	"id_customer":3,
	"nm_customer": "Amelia",
	"nr_cpf":"87521245842",
	"nr_rg":"16425453210",
	"nm_mother":"Emilia",
	"nm_father":"Sebastian",
	"nr_healthcare":"4305130",
	"ds_address":"rua das camelias",
    "nr_zipcode": "88644324321",
    "nr_adress": "69",
	"nr_telephone":"01989007691",
	"nr_cellphone":"0136554325",
	"ds_email":"amelia@mail.com",
	"dt_birthdate":"09/12/1999"
}
```

<br><hr><br>

**GET**: **_baseUrl_**/customers/{id}/sessions

Retorna todas a sessões que o cliente já fez

```json
   response 200

    {
        "id_customer":1,
        "nm_customer": "Roberto",
        "nr_cpf":"12545696585",
        "nr_rg":"36536548659",
        "nm_mother":"Maria",
        "nm_father":"João",
        "nr_healthcare":"2351254",
        "ds_address":"gaspar dutra",
        "nr_adress": "40",
        "nr_zipcode": "88644224581",
        "nr_telephone":"01989004591",
        "nr_cellphone":"0136558125",
        "ds_email":"roberto@mail.com",
        "dt_birthdate":"03/03/1995",
        "sessões": [
            {
                "id_session": 2,
                "id_customer": 1,
                "id_therapist": 1,
                "dt_start": "Wed, 03 Mar 2021 00:00:00 GMT",
                "dt_end": "Thu, 04 Mar 2021 00:00:00 GMT",
                "ds_status": "Ativada"
            },
            {
                "id_session": 3,
                "id_customer": 1,
                "id_therapist": 2,
                "dt_start": "Wed, 03 Mar 2021 00:00:00 GMT",
                "dt_end": "Thu, 04 Mar 2021 00:00:00 GMT",
                "ds_status": "Ativada"
            },
            {
                "id_session": 4,
                "id_customer": 1,
                "id_therapist": 3,
                "dt_start": "Wed, 03 Mar 2021 00:00:00 GMT",
                "dt_end": "Thu, 04 Mar 2021 00:00:00 GMT",
                "ds_status": "Ativada"
            }
        ]
    }
```

<br><hr><br>

**GET**: **_baseUrl_**/customers/{id}/customer_records

Retorna o prontuário do cliente com todas as técnicas

```json
   response 200

    {
        "nm_customer": "Frederic",
        "nr_cpf": "12312312302",
        "nr_rg": "3291113",
        "nm_mother": "Antonieta",
        "nm_father": "Frederic",
        "nr_healthcare": "31",
        "ds_address": "R. Austria",
        "nr_address": "22",
        "nr_zipcode": "7665444",
        "nr_telephone": "9900000003",
        "nr_cellphone": "8800000003",
        "ds_email": "copin@email.com",
        "dt_birthdate": "Wed, 01 Jan 1800 00:00:00 GMT",
        "sessões": [
            {
            "id_session": 3,
            "id_customer": 3,
            "id_therapist": 2,
            "dt_start": "Wed, 03 Mar 2021 00:00:00 GMT",
            "dt_end": "Thu, 04 Mar 2021 00:00:00 GMT",
            "ds_status": "agendada"
            }
        ]
    }
```

<br><hr><br>

**POST**: **_baseUrl_**/customers

Cadastra um novo cliente

**Important**

- **nr_cpf**, **nr_rg** e **ds_email** deve ser único para cada atendente;

```json
    request


    {
        "nm_customer": "Amelia",
        "nr_cpf":"87521245842",
        "nr_rg":"16425453210",
        "nm_mother":"Emilia",
        "nm_father":"Sebastian",
        "nr_healthcare":"4305130",
        "ds_address":"rua das camelias",
        "nr_zipcode": "88644324321",
        "nr_address": "69",
        "nr_telephone":"01989007691",
        "nr_cellphone":"0136554325",
        "ds_email":"amelia@mail.com",
        "dt_birthdate":"09/12/1999"
    }
```

```json
   response: 201

    {
        "id_customer":3,
        "nm_customer": "Amelia",
        "nr_cpf":"87521245842",
        "nr_rg":"16425453210",
        "nm_mother":"Emilia",
        "nm_father":"Sebastian",
        "nr_healthcare":"4305130",
        "ds_address":"rua das camelias",
        "nr_zipcode": "88644324321",
        "nr_address": "69",
        "nr_telephone":"01989007691",
        "nr_cellphone":"0136554325",
        "ds_email":"amelia@mail.com",
        "dt_birthdate":"09/12/1999"
    }
```

<br><hr><br>

**PATCH**: **_baseUrl_**/customers/{id}

Atualiza os dados de um cliente pelo seu id

**Important**

- **id_attendant** não pode ser atualizado

```json
    request:

    {
        "ds_email":"newemail@email.com",
    }
```

```json
   response 200

   {
        "id_attendant": 1,
        "nm_attendant": "John Doe",
        "nr_cpf": "12345678900",
        "nr_telephone": "9933331234",
        "nr_cellphone": "9999996789",
        "ds_email": "newemail@email.com",
        "ds_password": "123456",
        "dt_creation_time": "Thu, 09 Dec 2021 09:17:59 GMT",
        "id_clinic": 1
    }
```

<br><hr><br>

**DELETE**: **_baseUrl_**/customers/{id}

Deleta os dados de um cliente pelo seu id

```json
    response 204

    No body returned for response
```

<br><hr><br>

## /locations

Uma locação sempre estará atrelada a um terapeuta _(id_therapist)_, a uma clínica _(id_clinic)_ e a uma sala _(id_room)_. Sua estrutura é da seguinte forma:

- **"dt_start"**: data que se inicia a locação

- **"dt_end"**: data que se finaliza a locação

- **"id_room"**: id da sala que se quer locar
- **"id_clinic"**: id da clínica onde se vai alugar a sala
- **"id_therapist"**: id do terapeuta que está fazendo a locação

<br><hr><br>

**GET**: **_baseUrl_**/locations

Retorna a lista de locações

### **_Query Params_**

Esta rota aceita os seguintes parâmetros:

- **page**: número da página, por padrão retorna a página 1;
- **per_page**: limita a quantidade de locações por página, por padrão retorna 10;
- **dir**: direciona os dados de forma crescente ou decrescente;
- **order_by**: ordena por qualquer campo de locations
- **filt_por**: escolher um campo para filtrar
- **filt_valor**: escolher um valor do campo que se quer filtrar

O parâmetro _filt_por_ foi pensando para ser usado com datas, os campos 'dt*start' e 'dt_end' por exemplo, mas nada impede de ser usado por qualquer outro campo.
O parâmetro \_filt_valor* juntamente com _filt_por_ torna-se possível filtrar as locações por datas. Os dados retornam sempre da data escolhida em diante.

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

<br><hr><br>

**GET**: **_baseUrl_**/locations/id

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

<br><hr><br>

**GET**: **_baseUrl_**/locations/therapist/id

Retorna as locações pelo id do terapeuta

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

<br><hr><br>

**POST**: **_baseUrl_**/locations

Cadastra uma nova locação

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

<br><hr><br>

**PATCH**: **_baseUrl_**/locations/id

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
        "dt_end":"20/12/2021 13:00:00"

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

<br><hr><br>

**DELETE**: **_baseUrl_**/locations/id

Deleta um registro de locação

```json
    response 204

    No body returned for response
```

<br><hr><br>

## /rooms

Este endpoint trata de todos os registros das salas da clínica, as quais são possíveis alugar por dias ou horas. Cada Terapeuta precisa ter um sala para poder prestar serviçoes na Clínica.
Uma sala, tem a seguinte estrutura no banco de dados:

- **nm_room**: nome da sala - **string de no máximo 50 caracteres**
- **id_specialty**: id da specialty relacionada a essa sala - **numero inteiro**
- **ds_status**: status da situação da sala em relação a um locação **string de no máximo 15 caracteres**

<br><hr><br></br>

**GET**: **_baseUrl_**/rooms

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

<br><hr><br>

**GET**: **_baseUrl_**/rooms/{id}

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

<br><hr><br>

**GET**: **_baseUrl_**/rooms/status

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

<br><hr><br>

**GET**: **_baseUrl_**/rooms/schedule/id_room

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

<br><hr><br>

**POST**: **_baseUrl_**/rooms

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

<br><hr><br>

**PATCH**: **_baseUrl_**/attendants/{id}

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

<br><hr><br>

**DELETE**: **_baseUrl_**/rooms/{id}

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

<br><hr><br>

## /sessions

Uma 'session' é uma sessão administrada por um terapeuta com um cliente:

- **"id_customer"**: Id do cliente **"Um número inteiro"**

- **"id_therapist"**: Id do terapeuta **"Um número inteiro"**

- **"dt_start"**: Data e horário do ínicio da sessão **"Uma string no formato datetime com data e hora"**

- **"dt_end"**: Data e horário do fim da sessão **"Uma string no formato datetime com data e hora"**

- **"ds_status"**: Estado em que a sessão se encontra **"String de no máximo 15 caracteres"**

<br><hr><br>

**GET**: **_baseUrl_**/sessions/id

Retorna uma sessão pelo seu id.

Exemplo de url:
**_baseUrl_/sessions/3**

```json
   response 200

   {
    "id_session":3,
    "id_customer": 4,
	"id_therapist":1,
    "dt_start": "Fri, 12 Dec 2020 15:00:00 GMT",
    "dt_end": "Fri, 12 Dec 2020 16:00:00 GMT",
	"ds_status":"Confirmada"
    }
```

<br><hr><br>

**POST**: **_baseUrl_**/sessions

Cadastra uma nova sessão

```json
    request

    {
    "id_customer": 10,
	"id_therapist":8,
	"dt_start":"12/12/2020 15:00:00",
	"dt_end":"12/12/2020 16:00:00",
	"ds_status":"A confirmar"
    }
```

```json
   response: 201

   {
    "id_session": 1,
    "id_customer": 10,
	"id_therapist":8,
	"dt_start":"12/12/2020 15:00:00",
	"dt_end":"12/12/2020 16:00:00",
	"ds_status":"A confirmar"
    }
```

<br><hr><br>

**PATCH**: **_baseUrl_**/sessions/id

Atualiza os dados de uma sessão pelo seu id

**Important**

- É possível alterar qualquer informação da sessão, para caso haja erro de digitação ou discrepância no banco de dados

Exemplo de Url:
**_base_Url_/sessions/1**

```json
    request
    {
	"dt_start":"12/12/2020 19:00:00",
	"dt_end":"12/12/2020 20:00:00",
    "ds_status":"Confirmada"
    }
```

```json
    response 201

    {
    "id_session": 1,
    "id_customer": 10,
	"id_therapist":8,
	"dt_start":"12/12/2020 19:00:00",
	"dt_end":"12/12/2020 20:00:00",
	"ds_status":"Confirmada"
    }
```

<br><hr><br>

**DELETE**: **_baseUrl_**/sessions/id

Deleta um registro de uma sessão, deve se passar o numero de id da mesma, caso o id exista, a reposta será vazia com status code 204

Exemplo de Url:
**_base_Url_/sessions/7**

```json
    response 204
```

<br><hr><br>

## /specialties

Uma 'specialty' é uma especialidade de um terapeuta

- **"nm_specialty"**: Nome da especialidade **"Deve ser uma string de no máximo 50 caracteres"**

<br><hr><br>

**GET**: **_baseUrl_**/specialties

Retorna a lista de specialties

### **_Query Params_**

Esta rota aceita os seguintes parâmetros:

- **page**: número da página, por padrão retorna a página 1;
- **per_page**: limita a quantidade de locações por página, por padrão retorna 40;

```json
    response, 200
[
  {
    "id_specialty":1,
   	"nm_specialty": "Acumputura"
  },
  {
    "id_specialty":2,
   	"nm_specialty": "Reiki"
  }
]
```

<br><hr><br>

**POST**: **_baseUrl_**/specialties

Cadastra uma nova especialidade

- **campos unicos no banco de dados**: 'nm_specialty';

**Important**

```json
    request

    {
    "nm_specialty": "Reiki"
    }
```

```json
   response: 201

   {
    "id_specialty":1,
    "nm_specialty": "Reiki"
    }
```

<br><hr><br>

**PATCH**: **_baseUrl_**/specialties/id

Atualiza os dados de uma especialidade pelo seu id

Exemplo de Url:
**_base_Url_/specialties/3**

```json
    request
    {
	"nm_specialty":"Aromaterapia"
    }
```

```json
    response 201

    {
    "id_specialty":3,
    "nm_specialty": "Aromaterapia"
    }
```

<br><hr><br>

**DELETE**: **_baseUrl_**/specialties/id

Deleta uma especilidade, deve se passar o numero de id da mesma, caso o id exista, a reposta será vazia com status code 204

Exemplo de Url:
**_base_Url_/specialties/11**

```json
    response 204
```

<br><hr><br>

## /techniques

Uma 'technique' é uma técnica realizada em um cliente por um terapeuta e que está relacionada ao protuário do cliente:

- **"nm_technique"**: Nome da técnica **"String de no máximo 50 caracteres"**

- **"dt_start"**: Data e horário do ínicio da técnica **"String no formato datetime com data e hora"**

- **"dt_end"**: Data e horário do fim da técnica **"String no formato datetime com data e hora"**

- **"ds_comment"**: Comentário sobre o que foi realizada no técnica **"String de no máximo 1000 caracteres"**

- **"id_therapist"**: Id do terapeuta que aplicou a técnica **"Número inteiro"**

- **"id_customer_record"**: Id do prontuário do cliente **"Número inteiro"**

<br><hr><br>

**GET**: **_baseUrl_**/techniques

Retorna a lista de técnicas

```json
    response, 200
[
  {
    "id_technique": 4,
    "nm_technique": "Reiki",
    "dt_start": "Fri, 09 Dec 2022 00:00:00 GMT",
    "dt_end": "Fri, 09 Dec 2022 00:00:00 GMT",
    "ds_comment": "Técnica realizada com sucesso",
    "id_customer_record": 3,
    "id_therapist": 3
  },
  {
    "id_technique": 5,
    "nm_technique": "Reiki",
    "dt_start": "Fri, 09 Dec 2022 00:00:00 GMT",
    "dt_end": "Fri, 09 Dec 2022 00:00:00 GMT",
    "ds_comment": "Técnica realizada com sucesso",
    "id_customer_record": 3,
    "id_therapist": 3
  }
]
```

<br><hr><br>

**GET**: **_baseUrl_**/techniques/{id}

Retorna uma técnica pelo seu id.

```json
   response 200

     {
    "id_technique": 5,
    "nm_technique": "Reiki",
    "dt_start": "Fri, 09 Dec 2022 00:00:00 GMT",
    "dt_end": "Fri, 09 Dec 2022 00:00:00 GMT",
    "ds_comment": "Técnica realizada com sucesso",
    "id_customer_record": 3,
    "id_therapist": 3
     }
```

<br><hr><br>

**POST**: **_baseUrl_**/techniques

Cadastra uma nova técnica

**Important**

No cadastro da técnica é passa uma chave "nm_customer" com o valor do nome do cliente. A partir do nome do cliente a requisição salva no banco de dados o id do prontuário do cliente.

```json
    request

    {
	"nm_technique": "Reiki",
	"dt_start": "Fri, 09 Dec 2022 00:00:00 GMT",
    "dt_end": "Fri, 09 Dec 2022 00:00:00 GMT",
	"ds_comment": "Sucesso",
	"id_therapist": 3,
	"nm_customer":"Johan"
    }
```

```json
   response: 201

  {
    "id_technique": 5,
    "nm_technique": "Reiki",
    "dt_start": "Fri, 09 Dec 2022 00:00:00 GMT",
    "dt_end": "Fri, 09 Dec 2022 00:00:00 GMT",
    "ds_comment": "Sucesso",
    "id_customer_record": 3,
    "id_therapist": 3
  }
```

<br><hr><br>

**PATCH**: **_baseUrl_**/techniques/{id}

Atualiza os dados de uma técnica pelo seu id

**Important**

- É possível alterar qualquer informação da técnica, para caso haja erro de digitação ou discrepância no banco de dados

Exemplo de Url:
**_base_Url_/technique/3**

```json
    request
  {
    "ds_comment": "Houve um problema na execução da técnica"
  }
```

```json
    response 201
  {
    "id_technique": 5,
    "nm_technique": "Reiki",
    "dt_start": "Fri, 09 Dec 2022 00:00:00 GMT",
    "dt_end": "Fri, 09 Dec 2022 00:00:00 GMT",
    "ds_comment": "Houve um problema na execução da técnica",
    "id_customer_record": 3,
    "id_therapist": 3
  }
```

**DELETE**: **_baseUrl_**/techniques/{id}

Deleta um registro de uma técnica, deve se passar o numero de id da mesma, caso o id exista, a reposta será vazia com status code 204

Exemplo de Url:
**_base_Url_/technique/11**

```json
    response 204
```

<br><hr><br>

## /therapists

Um 'therapist' é um terapeuta que conduz as sessões com o cliente e aplica técnicas

- **id_therapist**: inteiro com id;
- **nm_therapist**: nome completo;
- **nr_cpf**: número do documento, deve ser uma string com 11 caracteres.
- **nr_crm**: número do registro do Conselho regional de Medicina, 4-10 digitos numéricos seguidos de '/' e 2 letras maiúsculas identificando o estado;
- **nr_cellphone**: número de telefone móvel, string com 10 ou 11 - DDD + número;
- **nm_user**: nome de usuário;
- **ds_email**: endereço de e-mail;
- **ds_password**: senha para acesso
- **ds_status**: indica o status, se o terapeuta esta atuando na clínica, por padrão o status é ativo;
- **fl_admin**: indica a flag, por padrão TRP, controla os níveis de acesso;
- **specialties**: lista com as especialidades

<br><hr><br>

**GET**: **_baseUrl_**/therapists

Traz a lista de todos os terapeutas.

**_Query Params_**

Esta rota aceita os seguintes parâmetros:

- **order_by**: ordena de forma crescente;
- **dir**: orienta a consulta de forma crescente('asc') ou decrescente('desc');
- **name**: consulta por nome do terapeuta;
- **status**: consulta por status;

Exemplo de url:
**_baseUrl/therapists?order_by=nm_therapist_&dir=desc**

```json
    response 200
    [
        {
        "id_therapist": 2,
        "nm_therapist": "Jung",
        "nr_cpf": "11122233301",
        "nr_crm": "123456781",
        "nr_cellphone": "9977771112",
        "nm_user": "self",
        "ds_email": "jung@mail.com",
        "ds_password": "123321",
        "ds_status": "ativo",
        "fl_admin": "TRP",
        "specialties": [
            {"nm_specialty":"Psicologia transcendental"}
        ]
    },
    {
        "id_therapist":1,
        "nm_therapist": "Freud",
        "nr_cpf": "11122233300",
        "nr_crm": "123456789",
        "nr_cellphone": "9977771111",
        "nm_user": "ego",
        "ds_email": "freud@mail.com",
        "ds_password": "123123",
        "ds_status": "ativo",
        "fl_admin": "TRP",
        "specialties": [
            {"nm_specialty":"Psicologia tradicional"}
        ]
    }
    ]
```

<br><hr><br>

**GET**: **_baseUrl_**/therapists/{id}

Retorna um terapeuta pelo seu id

```json
   response 200

    {
        "id_therapist":1,
        "nm_therapist": "Freud",
        "nr_cpf": "11122233300",
        "nr_crm": "123456789",
        "nr_cellphone": "9977771111",
        "nm_user": "ego",
        "ds_email": "freud@mail.com",
        "ds_password": "123123",
        "ds_status": "ativo",
        "fl_admin": "TRP",
        "specialties": [
            {"nm_specialty":"Psicologia tradicional"}
        ]
    }
```

<br><hr><br>

**GET**: **_baseUrl_**/therapists/{id}/schedule

Retorna a lista de consultas de um terapeuta pelo seu id

**_Query Params_**

Esta rota aceita os seguintes parâmetros:

- **order_by**: ordena de forma crescente;
- **dir**: orienta a consulta de forma crescente('asc') ou decrescente('desc');
- **status**: consulta por status;

Exemplo de url:
**\_baseUrl/therapists/1/schedule?status=agendado**

```json
   response 200

    [
        {
            "id_session": 4,
            "id_customer": 2,
            "id_therapist": 2,
            "dt_start": "Sun, 09 Jan 2022 13:40:00 GMT",
            "dt_end": "Mon, 10 Jan 2022 14:40:00 GMT",
            "ds_status": "agendado"
        }
    ]
```

<br><hr><br>

**POST**: **_baseUrl_**/therapists

Cadastra um novo terapeuta

**Important**

- **nr_cpf**,**nm_user**, **nm_crm**, **ds_email** devem ser únicos para cada terapeuta;
- se uma **specialty** não existir, é criado automaticamente;

```json
    request

    {
        "nm_therapist": "Freud",
        "nr_cpf": "11122233300",
        "nr_crm": "",
        "nr_cellphone": "9977771111",
        "nm_user": "ego",
        "ds_email": "freud@mail.com",
        "ds_password": "123123",
        "specialties": [
            {"nm_specialty":"Psicologia tradicional"}
    ]
  }
```

```json
   response: 201

   {
        "id_therapist":1,
        "nm_therapist": "Freud",
        "nr_cpf": "11122233300",
        "nr_crm": "123456789",
        "nr_cellphone": "9977771111",
        "nm_user": "ego",
        "ds_email": "freud@mail.com",
        "ds_password": "123123",
        "ds_status": "ativo",
        "fl_admin": "TRP",
        "specialties": [
            {"nm_specialty":"Psicologia tradicional"}
        ]
    }
```

<br><hr><br>

**PATCH**: **_baseUrl_**/therapists/{id}

Atualiza os dados de um terapeuta pelo seu id

**Important**

- **id_therapist** não podem ser atualizados

```json
    request:

    {
        "ds_email":"newemail@email.com",
    }
```

```json
   response 200

   {
        "id_therapist":1,
        "nm_therapist": "Freud",
        "nr_cpf": "11122233300",
        "nr_crm": "123456789",
        "nr_cellphone": "9977771111",
        "nm_user": "ego",
        "ds_email": "newemail@mail.com",
        "ds_password": "123123",
        "ds_status": "ativo",
        "fl_admin": "TRP",
        "specialties": [
            {"nm_specialty":"Psicologia tradicional"}
        ]
    }
```

<br><hr><br>

**DELETE**: **_baseUrl_**/therapists/{id}

Deleta os dados de um terapeuta pelo seu id

Exemplo de url:
**_baseUrl/therapists/1_**

```json
    response 204

    No body returned for response
```
