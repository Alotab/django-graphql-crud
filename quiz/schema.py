import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Quizzes, Question, Category, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "quiz")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")



class Query(graphene.ObjectType):
    
    #all_quizzes = DjangoListField(QuizzesType)
    #all_quizzes = graphene.List(QuizzesType)
    # all_quizzes = graphene.Field(QuizzesType, id = graphene.Int())
    # all_questions = graphene.List(QuestionType)

    ## query relations
    all_questions = graphene.Field(QuestionType, id = graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())


    def resolve_all_quetions(root, info, id):
        return Question.objects.get(pk=id)
    
    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)





class CreateCategoryMutation(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
    
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()

        return CreateCategoryMutation(category=category)
    

class UpdateCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(pk=id)
        category.name = name
        category.save()

        return UpdateCategoryMutation(category=category)
    


class DeleteCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(pk=id)
        category.delete()

        #return DeleteCategoryMutation(category=category)
        return




class Mutation(graphene.ObjectType):
    #create_category = CreateCategoryMutation.Field()
    #update_category = UpdateCategoryMutation.Field()
    delete_category =  DeleteCategoryMutation.Field()

schema  = graphene.Schema(query=Query, mutation=Mutation)