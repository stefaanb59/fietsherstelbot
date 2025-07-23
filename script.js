const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const chatLog = document.getElementById('chat-log');
const rasaEndpoint = 'http://localhost:5005/webhooks/rest/webhook'; // Zorg ervoor dat dit correct is

function toonBericht(bericht, isUser) {
    const berichtDiv = document.createElement('div');
    berichtDiv.classList.add(isUser ? 'user-message' : 'bot-message');
    berichtDiv.textContent = bericht;
    chatLog.appendChild(berichtDiv);
    chatLog.scrollTop = chatLog.scrollHeight; // Scroll naar de nieuwste berichten
}

async function stuurBericht() {
    const bericht = userInput.value.trim();
    if (bericht) {
        toonBericht(bericht, true); // Toon het bericht van de gebruiker

        try {
            const response = await fetch(rasaEndpoint, {
                method: 'POST', // **ZEER BELANGRIJK: Controleer of dit exact zo is geschreven**
                headers: {
                    'Content-Type': 'application/json', // **EN DEZE HEADER**
                },
                body: JSON.stringify({ message: bericht }), // **EN DE BODY ALS JSON**
            });

            const data = await response.json();
            if (data && data.length > 0 && data[0].text) {
                toonBericht(data[0].text, false); // Toon het antwoord van de bot
            } else {
                toonBericht('Er ging iets mis met het ophalen van het antwoord.', false);
            }
        } catch (error) {
            console.error('Fout bij het communiceren met de Rasa server:', error);
            toonBericht('Kan momenteel geen verbinding maken met de server.', false);
        }

        userInput.value = ''; // Leeg het inputveld
    }
}

// Event listeners
sendButton.addEventListener('click', stuurBericht);
userInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        stuurBericht();
    }
});