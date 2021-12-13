# /customers

Um 'customer' é o paciente que chegou na clínica e está querendo marcar uma consulta, ele é cadastrado por um atendente:

- **"nm_customer"**: Nome do paciente cadastrado **"Deve ser uma string de no máximo 50 caracteres"**

- **"nr_cpf"**: Número do cpf do paciente **"Uma string de no máximo 11 caracteres"**

- **"nr_rg"**: Número do cpf do paciente **"Uma string de no máximo 11 caracteres"**

- **"nm_mother"**&&**"nm_father"**: Nome da mãe e do pai do paciente **"String de no máximo 50 caracteres"**
- **"nr_healthcare"**: Numero do convenio do paciente **"String de no máximo 30 caracteres"**
- **"ds_adress"**: Endereço do paciente **"String de no máximo 50 caracteres"**

- **"nr_adress"**: Numero da casa do paciente **"String de no máximo 10 caracteres"**

- **"nr_zipcode"**: Numero do cep do paciente **"String de no máximo 10 caracteres"**
- **"nr_telefone"**&&**"nr_cellphone"**: Numero do telefone fixo e movel do paciente **"String de no máximo 11 caracteres"**
- **"ds_email"**: email do paciente **"String de no máximo 50 caracteres"**

## Atenção ao campo dt_end

- **"dt_birthdate"**: Data de nascimento **"Uma string no formato de data. Exemplo: 01/01/2010"** -**"IMPORTANTE"**:O formato da data precisa ir para o banco de dados no formato americano. Se a data vir por exemplo **"25/01/1998"**: A api não irá aceitar, porque ela entenderá que o 25 é o mês

<hr></br>

## **GET**: **_baseUrl_**/customers

Retorna a lista de customers

### **_Query Params_**

Esta rota aceita os seguintes parâmetros:

- **page**: número da página, por padrão retorna a página 1;
- **per_page**: limita a quantidade de locações por página, por padrão retorna 15;

Exemplo de url:
**_baseUrl_/locations?page=2&per_page=25**

\*_Se não for informado qualquer parâmetro a busca retorna todas as locações apenas_

```json
    response, 200
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

<hr></br>

## **GET**: **_baseUrl_**/customers/id

Retorna uma locação pelo seu id.

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

<hr></br>

## **GET**: **_baseUrl_**/customers/id/sessions

Retonna todas a consultas que o paciente já fez na clínica

Exemplo de url:
**_baseUrl_/locations/2/sessions**
Retorna todas as consultas que o paciente de id já fez

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

<hr></br>

## **GET**: **_baseUrl_**/customers/id/customer_records

Retonna todas a consultas que o paciente já fez na clínica

Exemplo de url:
**_baseUrl_/locations/3/customer_records**
Retorna o prontuário com todas as observações feitas pelos terapeutas a respeito desse paciente

```json
   response 200


    {
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
	"dt_birthdate": "Fri, 03 Mar 1999 00:00:00 GMT",
	"customer_records": []
}

```

<hr></br>

## **POST**: **_baseUrl_**/customers

Cadastra um novo paciente

**Important**

- **campos obrigatórios**: 'nm_customer', 'nr_cpf', 'ds_adress', 'nr_adress',dt_birthdate;
- os campos não obrigatórios devem seguir o seguinte formato: `{"any_key": ""}`
- **campos unicos no banco de dados**: 'nr_cpf', 'nr_rg', 'nr_healthcare';

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
    "nr_adress": "69",
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
    "nr_adress": "69",
	"nr_telephone":"01989007691",
	"nr_cellphone":"0136554325",
	"ds_email":"amelia@mail.com",
	"dt_birthdate":"09/12/1999"
    }
```

<hr></br>

## **PATCH**: **_baseUrl_**/customers/id

Atualiza os dados de uma locação pelo seu id

**Important**

- É possível alterar qualquer informação do paciente, para caso haja erro de digitação ou discrepância no banco de dados

Exemplo de Url:
**_base_Url_/customers/3**

```json
    request
{

	"nm_mother":"Dona Benta",
	"nm_father":"Viktor",

}
```

```json
    response 201

    {
    "id_customer":3,
    "nm_customer": "Amelia",
	"nr_cpf":"87521245842",
	"nr_rg":"16425453210",
	"nm_mother":"Dona Benta",
	"nm_father":"Viktor",
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

## **DELETE**: **_baseUrl_**/customers/id

Deleta um registro de paciente, deve se passar o numero de id do mesmo, caso o id resista, a reposta será vazia com status code 204

Exemplo de Url:
**_base_Url_/locations/11**

```json
    response 204
```
