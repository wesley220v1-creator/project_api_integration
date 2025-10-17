# Possiveis erros genéricos para a integração
class IntegrationError(Exception):
    """Erro genérico da integração"""
    pass

# Possiveis erros específico do Trello
class TrelloError(IntegrationError):
    pass

# Possiveis erros específico do Asana
class AsanaError(IntegrationError):
    pass
