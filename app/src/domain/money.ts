// Montants en unités mineures (centimes) pour éviter les erreurs d'arrondi.
// Les prix sont toujours calculés et figés par le serveur : le client ne fait que les afficher.
export type Currency = 'CAD' | 'EUR' | 'USD' | 'MAD' | 'DZD' | 'TND';

export interface Money {
  readonly amountMinor: number;
  readonly currency: Currency;
}

export function formatMoney(money: Money, locale = 'fr-CA'): string {
  return new Intl.NumberFormat(locale, { style: 'currency', currency: money.currency }).format(
    money.amountMinor / 100,
  );
}
