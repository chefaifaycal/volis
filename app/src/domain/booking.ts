// Machine d'états de réservation (affichage uniquement ; la source de vérité est le serveur).
export type BookingStatus =
  | 'requested'
  | 'accepted'
  | 'declined'
  | 'paid'
  | 'handed_over'
  | 'in_transit'
  | 'delivered'
  | 'released'
  | 'disputed'
  | 'cancelled';

const transitions: Readonly<Record<BookingStatus, readonly BookingStatus[]>> = {
  requested: ['accepted', 'declined', 'cancelled'],
  accepted: ['paid', 'cancelled'],
  declined: [],
  paid: ['handed_over', 'cancelled', 'disputed'],
  handed_over: ['in_transit', 'disputed'],
  in_transit: ['delivered', 'disputed'],
  delivered: ['released', 'disputed'],
  released: [],
  disputed: ['released', 'cancelled'],
  cancelled: [],
};

export function canTransition(from: BookingStatus, to: BookingStatus): boolean {
  return transitions[from].includes(to);
}

export const bookingStatusLabel: Readonly<Record<BookingStatus, string>> = {
  requested: 'En attente',
  accepted: 'Acceptée',
  declined: 'Refusée',
  paid: 'Payée (séquestre)',
  handed_over: 'Remis au voyageur',
  in_transit: 'En transit',
  delivered: 'Livré',
  released: 'Fonds versés',
  disputed: 'Litige en cours',
  cancelled: 'Annulée',
};
