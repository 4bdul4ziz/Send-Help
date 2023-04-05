#include <stdio.h>
#include <stdlib.h>

typedef enum TypeTag
{
    ADD,
    SUB,
    MUL,
    DIV,
    FIBO,
    CONST
} TypeTag;

typedef struct Node
{
    TypeTag type;
    int constValue;
} Node;

Node *addFunc(Node *a, Node *b)
{
    TypeTag type = ADD;
    Node *node = (Node *)malloc(sizeof(Node));
    node->type = type;
    node->constValue = a->constValue + b->constValue;
    return node;
}

Node *subFunc(Node *a, Node *b)
{
    TypeTag type = SUB;
    Node *node = (Node *)malloc(sizeof(Node));
    node->type = type;
    node->constValue = b->constValue - a->constValue;
    return node;
}

Node *mulFunc(Node *a, Node *b)
{
    TypeTag type = MUL;
    Node *node = (Node *)malloc(sizeof(Node));
    node->type = type;
    node->constValue = a->constValue * b->constValue;
    return node;
}

Node *divFunc(Node *a, Node *b)
{
    TypeTag type = DIV;
    Node *node = (Node *)malloc(sizeof(Node));
    node->type = type;
    node->constValue = a->constValue / b->constValue;
    return node;
}

Node *fibonacci(Node *n, Node *m);

Node *(*makeFunc(TypeTag type))(Node *, Node *)
{
    Node *(*func)(Node *, Node *);
    switch (type)
    {
    case ADD:
        func = &addFunc;
        break;
    case SUB:
        func = &subFunc;
        break;
    case MUL:
        func = &mulFunc;
        break;
    case DIV:
        func = &divFunc;
        break;
    case FIBO:
        func = &fibonacci;
        break;
    default:
        func = NULL;
    }
    return func;
}

int fibonacciCache[100];

void initializeCache()
{
    for (int i = 0; i < 100; i++)
    {
        fibonacciCache[i] = -1;
    }
}
int fibonacciValue(int n)
{
    if (n < 0)
        n = 1;
    if (n <= 1)
        return n;
    if (fibonacciCache[n] != -1)
    {
        return fibonacciCache[n];
    }
    fibonacciCache[n] = fibonacciValue(n - 1) + fibonacciValue(n - 2);
    return fibonacciCache[n];
}

Node *fibonacci(Node *n, Node *m)
{
    TypeTag type = FIBO;
    Node *node = (Node *)malloc(sizeof(Node));
    node->type = type;
    if (n == NULL)
        node->constValue = 1;
    else 
        node->constValue = fibonacciValue(n->constValue) + fibonacciValue(n->constValue - 1);
        return node;

}

void calc(Node *node)
{
    if (node->type == ADD)
    {
        printf("Add: %d\n", node->constValue);
    }
    else if (node->type == SUB)
    {
        printf("Sub: %d\n", node->constValue);
    }
    else if (node->type == MUL)
    {
        printf("Mul: %d\n", node->constValue);
    }
    else if (node->type == DIV)
    {
        printf("Div: %d\n", node->constValue);
    }
    else if (node->type == FIBO)
    {
        printf("Fibo: %d\n", node->constValue);
    }
}

int main()
{
    initializeCache();
    Node *add_a = (Node *)malloc(sizeof(Node));
    add_a->type = CONST;
    add_a->constValue = 10;

    Node *add_b = (Node *)malloc(sizeof(Node));
    add_b->type = CONST;
    add_b->constValue = 6;

    Node *add = (*makeFunc(ADD))(add_a, add_b);
    calc(add);

    Node *mul_a = (Node *)malloc(sizeof(Node));
    mul_a->type = CONST;
    mul_a->constValue = 5;

    Node *mul_b = (Node *)malloc(sizeof(Node));
    mul_b->type = CONST;
    mul_b->constValue = 4;

    Node *mul = (*makeFunc(MUL))(mul_a, mul_b);
    calc(mul);

    Node *sub = (*makeFunc(SUB))(mul, add);
    calc(sub);

    Node *fibo = (*makeFunc(FIBO))(sub, NULL);
    calc(fibo);


    free(add_a);
    free(add_b);
    free(add);
    free(mul_a);
    free(mul_b);
    free(mul);
    free(sub);
    free(fibo);
    return 0;
}
