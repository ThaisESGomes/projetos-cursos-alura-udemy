let display = document.getElementById('result');
let historyList = document.getElementById('history-list');
let currentInput = '';
let operator = '';
let previousInput = '';
let history = [];

function appendToDisplay(value) {
    if (display.value === '0' || display.value === 'Erro') {
        display.value = '';
    }
    
    if (['+', '-', '*', '/'].includes(value)) {
        if (currentInput !== '') {
            if (previousInput !== '' && operator !== '') {
                calculate();
            }
            previousInput = currentInput;
            operator = value;
            currentInput = '';
            display.value += ` ${value} `;
        }
    } else {
        currentInput += value;
        display.value += value;
    }
}

function clearDisplay() {
    display.value = '';
    currentInput = '';
    operator = '';
    previousInput = '';
}

function deleteLast() {
    let currentValue = display.value;
    if (currentValue.length > 0) {
        display.value = currentValue.slice(0, -1);
        if (currentInput.length > 0) {
            currentInput = currentInput.slice(0, -1);
        }
    }
}

function calculate() {
    if (previousInput !== '' && currentInput !== '' && operator !== '') {
        let num1 = parseFloat(previousInput);
        let num2 = parseFloat(currentInput);
        let result;
        
        switch (operator) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                if (num2 === 0) {
                    display.value = 'Erro';
                    resetCalculator();
                    return;
                }
                result = num1 / num2;
                break;
            default:
                return;
        }
        
        // Arredondar para 8 casas decimais para evitar problemas de precisão
        result = Math.round(result * 100000000) / 100000000;
        
        // Adicionar ao histórico
        let operation = `${previousInput} ${operator} ${currentInput} = ${result}`;
        addToHistory(operation);
        
        display.value = result;
        currentInput = result.toString();
        operator = '';
        previousInput = '';
    }
}

function addToHistory(operation) {
    history.unshift(operation);
    
    // Manter apenas os últimos 10 cálculos
    if (history.length > 10) {
        history.pop();
    }
    
    updateHistoryDisplay();
}

function updateHistoryDisplay() {
    historyList.innerHTML = '';
    history.forEach(operation => {
        let li = document.createElement('li');
        li.textContent = operation;
        historyList.appendChild(li);
    });
}

function resetCalculator() {
    currentInput = '';
    operator = '';
    previousInput = '';
}

// Suporte para teclado
document.addEventListener('keydown', function(event) {
    const key = event.key;
    
    if (key >= '0' && key <= '9' || key === '.') {
        appendToDisplay(key);
    } else if (['+', '-', '*', '/'].includes(key)) {
        appendToDisplay(key);
    } else if (key === 'Enter' || key === '=') {
        event.preventDefault();
        calculate();
    } else if (key === 'Escape' || key === 'c' || key === 'C') {
        clearDisplay();
    } else if (key === 'Backspace') {
        deleteLast();
    }
});

// Inicializar display
clearDisplay();

