from src.domain.shared.aggregate_root_interface import AggregateRootInterface
from src.domain.exceptions.domain_exception import DomainException


class User(AggregateRootInterface):
    """Representa um usuário, raiz do agregado."""

    def __init__(self, uid: str, name: str, email: str, password: str):
        """Inicializa o usuário com um ID e nome."""
        
        if not uid.strip():
            raise DomainException("O id do usuário não pode estar vazio.")
        
        if not name.strip():
            raise DomainException("O nome do usuário não pode estar vazio.")
        
        if not email.strip():
            raise DomainException("O e-mail do usuário não pode estar vazio.")
        
        if not password.strip():
            raise DomainException("A senha do usuário não pode estar vazio.")
        
        super().__init__(uid)
        self.name = name
        self.email = email
        self.password = password