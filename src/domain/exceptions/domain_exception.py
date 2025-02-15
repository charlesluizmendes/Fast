class DomainException(ValueError):
    """Exceção para erros de domínio."""
    
    def __init__(self, message: str):
        """Inicializa a exceção com uma mensagem."""
        self.message = message
        super().__init__(message)

    def __str__(self):
        """Retorna a mensagem de erro."""
        return self.message
