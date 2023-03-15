# django-graphql-crud



## Query to fetch data from the server

```
query {
    allQuizzes{
        id
        title
    }
}
```

```
query {
  allQuizzes{
    id
    title
  }
	allQuestions{
    title
  }
}
```

`Query using id`

```
query {
  allQuizzes(id:1){
    id
    title
  }
}
```

`Query using foreign key`

```
query {
  allQuestions(id: 1){
    title
  }
  allAnswers(id: 1){
    answerText
  }
}

```

`Send data to the backend or server / mutation`

```
mutation {
	updateCategory(name: "newcat") {
    category {
      name
    }
  }
}
```