## Clinicas

Todas as clínicas são listadas e/ou criadas com os seguintes dados:

```json
{
  "nm_clinic": "nome_da_clinica",
  "nr_cnpj": "número do cnpj no formato 12123123/000112",
  "ds_address": "rua onde está localizada",
  "nr_number": "número do prédio",
  "ds_complement": "número da sala (caso houver)",
  "ds_district": "cidade",
  "nr_zipcode": "número postal no formato: 12123-123",
  "ds_city": "cidade",
  "ds_uf": "UF do estado",
  "ds_email": "email da clínica, não sendo possível cadastrar o mesmo email para duas clínicas diferentes",
  "nr_telephone": "número de telefone fixo",
  "nr_cellphone": "número de celular"
}
```

<hr>

**GET**: **base_url**/clinics

Retorna todas as clínicas cadastradas

**Exemplo de retorno**:

```json
[
  {
    "id_clinic": 1,
    "nm_clinic": "QantMed",
    "nr_cnpj": "123456789876543",
    "ds_address": "R. de schrödinger",
    "nr_number": 40,
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
    "nr_number": "456",
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
    "nr_number": "789",
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

<hr>

**GET POR ID**: **base_url**/clinics/clinic_id

Retorna uma clinica expecificamente

**Exemplo de retorno para o id 1**:

```json
{
  "id_clinic": 1,
  "nm_clinic": "QantMed",
  "nr_cnpj": "123456789876543",
  "ds_address": "R. de schrödinger",
  "nr_number": 40,
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

Caso o **id** não exista a seguinte mensagem de erro, com o código 404 será retornada:

```json
{
  "erro": "Clínica não existe"
}
```

<hr>

**Post**: **base_url**/clinics

Para cadastrar uma nova clínica é necessário informar todos os dados que são listados no método **GET**

**Exemplo de um corpo de requisição para cadastro:**

```json
{
  "nm_clinic": "QantMed",
  "nr_cnpj": "123456789876543",
  "ds_address": "R. de schrödinger",
  "nr_number": 40,
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

Caso aluma chave inválida seja passada na hora da requisição a seguinte mensagem de erro com o código 400 retornará:

```json
{
  "Error": {
    "Chaves_erradas": ["nr_whatsapp"],
    "Chaves Disponíveis": [
      "ds_email",
      "nm_clinic",
      "nr_number",
      "ds_district",
      "nr_cnpj",
      "ds_city",
      "nr_telephone",
      "ds_uf",
      "nr_zipcode",
      "nr_cellphone",
      "ds_address",
      "ds_complement"
    ]
  }
}
```

<hr>

**PATCH**: **base_url**/clinics/id_clinic

Para atualizar algum dado de sua clínica é necessário informar o respectivo id, para descobrí-lo pode-se utilizar a rota **GET**

**Exemplo de uma requisição PATCH**

```json
{
  "ds_uf": "SP"
}
```

O retorno será todos os dados da respectiva clínica com o dado atualizado:

```json
{
  "id_clinic": 1,
  "nm_clinic": "QantMed",
  "nr_cnpj": "123456789876543",
  "ds_address": "R. de schrödinger",
  "nr_number": 40,
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

Caso uma chave inexistente seja passada a seguinte mensagem de erro junto com o código 400 será retornado:

**Requisição**:

```json
{
  "estado": "SP"
}
```

**Retorno**

```json
{
  "erro": {
    "Chaves_erradas": ["estado"],
    "Chaves Disponíveis": [
      "ds_email",
      "nm_clinic",
      "nr_number",
      "ds_district",
      "nr_cnpj",
      "ds_city",
      "nr_telephone",
      "ds_uf",
      "nr_zipcode",
      "nr_cellphone",
      "ds_address",
      "ds_complement"
    ]
  }
}
```

<hr>

**DELETE**: **base_url**/clinics/clinic_id

Para excluir uma clínica basta passar o respectivo id, não será retornado nenhum corpo apenas o código 204
