class DomainException(Exception):
    """Exceção para erros de domínio."""
    message: str

    def __str__(self):
        """Retorna a mensagem de erro."""
        return self.message
