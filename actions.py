from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGeefHerstelling(Action):
    def name(self) -> Text:
        return "action_geef_herstelling"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent = tracker.latest_message['intent'].get('name')
        herstel_info = {
            "rem_afstellen": (
                "➡️ Rem afstellen (algemeen):\n"
                "1. Controleer de kabelspanning: deze moet correct zijn voor het type rem.\n"
                "2. Zorg ervoor dat de remblokken of remschoenen goed uitgelijnd zijn met het remoppervlak (velg of schijf).\n"
                "3. Stel de afstand van de remblokken/schoenen tot het remoppervlak af met de stelschroeven of andere mechanismen.\n"
                "4. Controleer of de remmen niet slepen wanneer ze niet worden ingedrukt.\n"
                "5. Test de remwerking: de remmen moeten effectief en veilig tot stilstand komen.\n"
                "ℹ️ Let op: De specifieke stappen kunnen variëren afhankelijk van het type rem (V-brake, schijfrem, cantilever, etc.). Raadpleeg indien nodig een specifieke handleiding voor jouw type rem."
            ),
            "voorderailleur_afstellen": (
                "➡️ Voorderailleur afstellen:\n"
                "1. Zet ketting op kleinste kettingblad voor en grootste tandwiel achter.\n"
                "2. Stel L-schroef af zodat ketting niet tegen kooi loopt.\n"
                "3. Zet ketting op grootste kettingblad en kleinste tandwiel achter.\n"
                "4. Stel H-schroef af zodat ketting niet tegen kooi loopt.\n"
                "5. Controleer middenpositie en kabelspanning.\n"
                "6. Test schakelgedrag en stel eventueel bij."
            ),
            "pedalen_vervangen": (
                "➡️ Pedalen vervangen:\n"
                "1. Gebruik een pedaalsleutel of inbussleutel.\n"
                "2. Linkerpedaal heeft linkse draad (links losdraaien).\n"
                "3. Draai beide pedalen los.\n"
                "4. Reinig schroefdraad en breng vet aan.\n"
                "5. Monteer nieuwe pedalen: rechts met de klok mee, links tegen de klok in.\n"
                "6. Draai stevig vast.\n"
                "7. Test op kraak- of spelinggeluiden."
            ),
            "crankas_vervangen": (
                "➡️ Crankas vervangen:\n"
                "1. Verwijder pedalen.\n"
                "2. Demonteer crankarmen met cranktrekker.\n"
                "3. Verwijder oude crankas met geschikt gereedschap.\n"
                "4. Reinig het trapashuis.\n"
                "5. Plaats nieuwe crankas (let op schroefdraadtype: BSA/ITA).\n"
                "6. Draai aan met juiste aanhaalmoment.\n"
                "7. Monteer crankarmen opnieuw, goed invetten.\n"
                "8. Plaats pedalen terug.\n"
                "9. Test trapbeweging op speling."
            ),
            "stuur_verhogen": (
                "➡️ Stuur verhogen:\n"
                "1. Controleer type stuurpen: quill of Ahead.\n"
                "2. Bij quill: bout bovenop losdraaien, tik lichtjes, trek omhoog.\n"
                "3. Bij Ahead: bouten los, spacers toevoegen of stuurpen verplaatsen.\n"
                "4. Alles aandraaien met juiste kracht.\n"
                "5. Controleer uitlijning en test soepelheid."
            ),
            "ketting_vervangen": (
                "➡️ Ketting vervangen:\n"
                "1. Schakel naar kleinste tandwielen.\n"
                "2. Zoek missing link of verwijder schakel met kettingpons.\n"
                "3. Meet nieuwe ketting: 2 schakels extra bij volledig gestrekte ketting.\n"
                "4. Kort ketting in.\n"
                "5. Leg ketting correct om tandwielen.\n"
                "6. Verbind ketting met missing link of klink schakel.\n"
                "7. Test soepelheid en schakelen."
            ),
            "cassette_vervangen": (
                "➡️ Cassette vervangen:\n"
                "1. Verwijder achterwiel.\n"
                "2. Gebruik cassetteafnemer en kettingzweep om lockring los te draaien.\n"
                "3. Reinig body.\n"
                "4. Plaats nieuwe cassette.\n"
                "5. Lockring stevig vastdraaien.\n"
                "6. Monteer wiel en test schakelen."
            ),
            "freewheel_vervangen": (
                "➡️ Freewheel vervangen:\n"
                "1. Verwijder achterwiel.\n"
                "2. Gebruik passende freewheelafnemer.\n"
                "3. Draai freewheel los.\n"
                "4. Reinig wielschroefdraad.\n"
                "5. Plaats nieuwe freewheel, handvast.\n"
                "6. Monteer wiel.\n"
                "7. Test trappen en remmen."
            ),
            "achterderailleur_afstellen": (
                "➡️ Achterderailleur afstellen:\n"
                "1. Zet ketting op kleinste achtertandwiel.\n"
                "2. Stel H-schroef af zodat derailleurwieltjes netjes onder kleinste tandwiel staan.\n"
                "3. Schakel naar grootste achtertandwiel.\n"
                "4. Stel L-schroef af zodat derailleurwieltjes netjes onder grootste tandwiel staan.\n"
                "5. Pas kabelspanning aan indien nodig.\n"
                "6. Controleer B-schroef (afstand derailleur/cassette).\n"
                "7. Test schakelen door alle versnellingen."
            )
        }

        if intent in herstel_info:
            dispatcher.utter_message(text=herstel_info[intent])
        else:
            dispatcher.utter_message(text="Sorry, ik heb geen informatie over hoe je dat moet herstellen.")

        return []