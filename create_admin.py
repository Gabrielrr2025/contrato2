from auth import create_user

# Cria usuário admin padrão
# login: admin / senha: admin123
create_user("admin", "admin123", is_admin=True)

print("✅ Usuário admin criado com sucesso (login=admin / senha=admin123)")
