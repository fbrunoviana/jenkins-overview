# Gerenciamento de Usuários, Roles e Matrix no Jenkins

O Jenkins permite o gerenciamento eficaz de usuários e controle de acesso granular para garantir a segurança e a correta funcionalidade do sistema.

## Parte 1: Gerenciamento de Usuários

### Etapa 1: Adicionar Usuários

1. Vá para "Gerenciar Jenkins" > "Gerenciar Usuários" > "Criar Usuário".
2. Preencha os campos Nome de usuário, Senha, Confirmação de senha, Nome completo e Endereço de e-mail e clique em "Criar usuário".

### Etapa 2: Modificar Usuários

1. Vá para "Gerenciar Jenkins" > "Gerenciar Usuários".
2. Clique no nome do usuário que deseja modificar.
3. Clique em "Configurar" para alterar os detalhes do usuário.

### Etapa 3: Remover Usuários

1. Vá para "Gerenciar Jenkins" > "Gerenciar Usuários".
2. Clique no nome do usuário que deseja remover.
3. Clique em "Excluir" para remover o usuário.

## Parte 2: Gerenciamento de Roles (Funções)

O gerenciamento de roles ou funções permite controlar o acesso dos usuários a diferentes partes do Jenkins. Para usar este recurso, é necessário instalar o plugin "Role-based Authorization Strategy". 

### Etapa 1: Definir Funções

1. Vá para "Gerenciar Jenkins" > "Manage and Assign Roles" > "Manage Roles".
2. Aqui você pode definir roles para Usuários, Nodes e Projetos.

### Etapa 2: Atribuir Funções

1. Vá para "Gerenciar Jenkins" > "Manage and Assign Roles" > "Assign Roles".
2. Aqui você pode atribuir os roles que definiu aos Usuários, Nodes e Projetos.

## Parte 3: Matrix de Segurança

A matrix de segurança oferece uma forma mais detalhada de controle de acesso em comparação com as funções baseadas em roles. Para usá-la, você deve ter o plugin "Matrix Authorization Strategy" instalado.

1. Vá para "Gerenciar Jenkins" > "Configure Global Security".
2. Em "Authorization", selecione "Matrix-based security".
3. Aqui você pode adicionar usuários ou grupos e definir permissões específicas para eles. 

Seja cuidadoso ao usar a matrix de segurança para não revogar acidentalmente seu próprio acesso.

Gerenciar usuários, roles e a matrix de segurança é uma parte fundamental do gerenciamento do Jenkins, permitindo o controle granular de permissões e acesso aos recursos do Jenkins.
