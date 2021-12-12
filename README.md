# Quantic Med

Aplicação direcionada para o gerenciamento de uma clínica de terapias holísticas.

## Introdução

PESQUISAR

## Prefixos

O que é nm?

## /attendants

(TODO: melhorar descricao, descrever mais detalhadamente!)
Corpo da requisição:

- **nm_attendant**: nome completo do colaborador/recepcionista
- **nr_cpf**: número do documento, deve ser uma string com 11 caracteres.
- **nr_telephone**: número de telefone residencial, string com 10 caracteres - DDD + número
- **nr_cellphone**: número de telefone móvel, string com 10 ou 11 - DDD + número
- **ds_email**: endereço de e-mail
- **ds_password**: senha para acesso, no mínimo 6 caracteres
- **dt_creation_time**: data da criação do recepcionista;
- **id_clinic**: id(inteiro) da clínica onde o colaborador atua

<hr>

**GET**: **_baseUrl_**/attendants

Traz a lista de terapeutas.Por padrão retorna 5 por página.

**_Query Params_**

Esta rota aceita os seguintes parâmetros:

- **page**: número da página, por padrão retorna a página 1;
- **per_page**: limita a quantidade de terapeutas por página, por padrão retorna 5;
- **order_by**: ordena de forma crescente;
- **dir**: orienta a consulta de forma crescente('asc') ou decrescente('desc');
- **name**: consulta por nome do terapeuta;

Exemplo de url:
**_baseUrl/attendants?page=1&per_page=2&order_by=nm_attendant_**

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

<hr>

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

<hr>

**POST**: **_baseUrl_**/attendants

Cadastra um novo recepcionista

**Important**

- **campos obrigatórios**: 'nm_attendant', 'nr_cpf', 'id_clinic';
- os campos não obrigatórios devem seguir o seguinte formato: `{"any_key": ""}`
- **nr_cpf** deve ser único para cada atendente;
- **_nr_cpf_**,**_nr_cellphone_**,**_nr_telephone_** devem conter somente os números;
- **_ds_password_** deve conter no mínimo 6 caracteres;

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

<hr>

**PATCH**: **_baseUrl_**/attendants/{id}

Atualiza os dados de um recepcionista pelo seu id

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

<hr>

**DELETE**: **_baseUrl_**/attendants/{id}

Deleta os dados de um recepcionista pelo seu id

Exemplo de url:
**_baseUrl/attendants/1_**

```json
    response 204

    No body returned for response
```

## /therapists

Dados de um terapeuta:

- **id_therapist**: inteiro com id;
- **nm_therapist**: nome completo;
- **nr_cpf**: número do documento, deve ser uma string com 11 caracteres.
- **nr_crm**: número do registro do Conselho regional de Medicina, string com 15 caracteres;
- **nr_cellphone**: número de telefone móvel, string com 10 ou 11 - DDD + número;
- **nm_user**: nome de usuário;
- **ds_email**: endereço de e-mail;
- **ds_password**: senha para acesso, no mínimo 6 caracteres;
- **ds_status**: indica o status, se o terapeuta esta atuando na clínica, por padrão o status é ativo;
- **fl_admin**: indica a flag, por padrão TRP, controla os níveis de acesso;
- **specialties**: lista com as especialidades

<hr>

**GET**: **_baseUrl_**/therapists

Traz a lista de terapeutas.Por padrão retorna 5 por página.

**_Query Params_**

Esta rota aceita os seguintes parâmetros:

- **page**: número da página, por padrão retorna a página 1;
- **per_page**: limita a quantidade de terapeutas por página, por padrão retorna 5;
- **order_by**: ordena de forma crescente;
- **dir**: orienta a consulta de forma crescente('asc') ou decrescente('desc');
- **name**: consulta por nome do terapeuta;
- **status**: consulta por status;

Exemplo de url:
**_baseUrl/therapists?page=1&per_page=2&order_by=nm_therapist_&dir=desc**

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

<hr>

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

<hr>

**GET**: **_baseUrl_**/therapists/{id}

Retorna a lista de consultas de um terapeuta pelo seu id, por padrao retorna uma lista com as 20 consultas agendadas recentemente

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

<hr>

**POST**: **_baseUrl_**/therapists

Cadastra um novo recepcionista

**Important**

- **campos obrigatórios**: 'nm_therapist', 'nr_cpf', 'ds_email';
- os campos não obrigatórios devem seguir o seguinte formato: `{"any_key": ""}`
- **nr_cpf**,**nm_user** devem ser únicos para cada terapeuta;
- **_nr_cpf_**,**_nr_cellphone_** devem conter somente os números;
- **_ds_password_** deve conter no mínimo 6 caracteres;
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

<hr>

**PATCH**: **_baseUrl_**/therapists/{id}

Atualiza os dados de um recepcionista pelo seu id

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

<hr>

**DELETE**: **_baseUrl_**/therapists/{id}

Deleta os dados de um recepcionista pelo seu id

Exemplo de url:
**_baseUrl/therapists/1_**

```json
    response 204

    No body returned for response
```
