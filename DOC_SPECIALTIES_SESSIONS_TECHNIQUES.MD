# /specialties

Uma 'specialty' é uma especialidade de um terapeuta

- **"nm_specialty"**: Nome da especialidade **"Deve ser uma string de no máximo 50 caracteres"**

<hr></br>

## **GET**: **_baseUrl_**/specialties

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

<hr></br>

## **POST**: **_baseUrl_**/specialties

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

<hr></br>

## **PATCH**: **_baseUrl_**/specialties/id

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

<hr></br>

## **DELETE**: **_baseUrl_**/specialties/id

Deleta uma especilidade, deve se passar o numero de id da mesma, caso o id exista, a reposta será vazia com status code 204

Exemplo de Url:
**_base_Url_/specialties/11**

```json
    response 204
```

<hr></br>

# /sessions

Uma 'session' é uma sessão administrada por um terapeuta com um cliente:

- **"id_customer"**: Id do cliente **"Um número inteiro"**

- **"id_therapist"**: Id do terapeuta **"Um número inteiro"**

- **"dt_start"**: Data e horário do ínicio da sessão **"Uma string no formato datetime com data e hora"**

- **"dt_end"**: Data e horário do fim da sessão **"Uma string no formato datetime com data e hora"**

- **"ds_status"**: Estado em que a sessão se encontra **"String de no máximo 15 caracteres"**

## Atenção aos campos dt_start, dt_end

- **"dt_start, dt_end"**: Data e horário do início e fim da sessão respectivamente **"Uma string no formato de data. Exemplo: 01/01/2010 10:40:51"** -**"IMPORTANTE"**:O formato da data precisa ir para o banco de dados no formato americano. Se a data vir por exemplo **"25/01/1998"**: A api não irá aceitar, porque ela entenderá que o 25 é o mês

<hr></br>

## **GET**: **_baseUrl_**/sessions/id

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

<hr></br>

## **POST**: **_baseUrl_**/sessions

Cadastra uma nova sessão

**Important**

- **campos obrigatórios**: 'id_customer', 'id_therapist', 'dt_start';
- os campos não obrigatórios devem seguir o seguinte formato: `{"any_key": ""}`

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

<hr></br>

## **PATCH**: **_baseUrl_**/sessions/id

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

<hr></br>

## **DELETE**: **_baseUrl_**/sessions/id

Deleta um registro de uma sessão, deve se passar o numero de id da mesma, caso o id exista, a reposta será vazia com status code 204

Exemplo de Url:
**_base_Url_/sessions/7**

```json
    response 204
```

<hr></br>

# /technique

Uma 'technique' é uma técnica realizada em um cliente por um terapeuta e que está relacionada ao protuário do cliente:

- **"nm_technique"**: Nome da técnica **"String de no máximo 50 caracteres"**

- **"dt_start"**: Data e horário do ínicio da técnica **"String no formato datetime com data e hora"**

- **"dt_end"**: Data e horário do fim da técnica **"String no formato datetime com data e hora"**

- **"ds_comment"**: Comentário sobre o que foi realizada no técnica **"String de no máximo 1000 caracteres"**

- **"id_therapist"**: Id do terapeuta que aplicou a técnica **"Número inteiro"**

- **"id_customer_record"**: Id do prontuário do cliente **"Número inteiro"**

## Atenção aos campos dt_start, dt_end

- **"dt_start, dt_end"**: Data e horário do início e fim da sessão respectivamente **"Uma string no formato de data. Exemplo: 01/01/2010 10:40:51"** -**"IMPORTANTE"**:O formato da data precisa ir para o banco de dados no formato americano. Se a data vir por exemplo **"25/01/1998"**: A api não irá aceitar, porque ela entenderá que o 25 é o mês

<hr></br>

## **GET**: **_baseUrl_**/technique

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

<hr></br>

## **GET**: **_baseUrl_**/technique/id

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

<hr></br>

## **POST**: **_baseUrl_**/technique

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

<hr></br>

## **PATCH**: **_baseUrl_**/technique/id

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

## **DELETE**: **_baseUrl_**/technique/id

Deleta um registro de uma técnica, deve se passar o numero de id da mesma, caso o id exista, a reposta será vazia com status code 204

Exemplo de Url:
**_base_Url_/technique/11**

```json
    response 204
```
