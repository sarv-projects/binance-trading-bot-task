def validate_input(symbol, side, order_type, quantity, price):
    errors = []
    
    if not symbol or not isinstance(symbol, str):
        errors.append("Symbol cannot be empty.")
        
    if side not in ['BUY', 'SELL']:
        errors.append("Side must be BUY or SELL.")
        
    if order_type not in ['MARKET', 'LIMIT']:
        errors.append("Order Type must be MARKET or LIMIT.")
        
    if quantity <= 0:
        errors.append("Quantity must be positive.")
        
    if order_type == 'LIMIT' and (price is None or price <= 0):
        errors.append("Price is required for LIMIT orders.")

    return errors