# Quantic Med

Aplicação direcionada para o gerenciamento de uma clínica de terapias holísticas.

## /attendants

<hr>

**GET**: **_baseUrl_**/attendants

Traz a lista de recepcionistas.Por padrão retorna 5 por página.

**_Query Params_**

Esta rota aceita os seguintes parâmetros:

- **page**: número da página, por padrão retorna a página 1;
- **per_page**: limita a quantidade de recepcionistas por página, por padrão retorna 5;
- **order_by**: ordena de forma crescente;

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

Corpo da requisição:

- **nm_attendant**: nome completo do colaborador/recepcionista
- **nr_cpf**: número do documento - CPF
- **nr_telephone**: número de telefone residencial - campo não obrigatório
- **nr_cellphone**: número de telefone móvel
- **ds_email**: endereço de e-mail
- **ds_password**: senha para acesso
- **id_clinic**: id da clínica onde o colaborador atua

**Important**

- **campos obrigatórios**: 'nm_attendant', 'nr_cpf', 'id_clinic';
- os campos não obrigatórios devem seguir o seguinte formato: `{"anyone_key": ""}`
- **nr_cpf** deve ser único para cada atendente;
- **_nr_cpf_**,**_nr_cellphone_**,**_nr_telephone_** devem conter somente os números;
- **_ds_password_** deve conter no mínimo 6 caracteres;

```json
    request 201

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
   response:

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
