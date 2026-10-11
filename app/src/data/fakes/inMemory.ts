import type { Repositories } from '../repositories/types';

// Données fictives et illustratives (aucune donnée réelle) en attendant le backend Supabase.
const montreal = { city: 'Montréal', countryCode: 'CA', airportCode: 'YUL' } as const;
const paris = { city: 'Paris', countryCode: 'FR', airportCode: 'CDG' } as const;
const casablanca = { city: 'Casablanca', countryCode: 'MA', airportCode: 'CMN' } as const;

export const inMemoryRepositories: Repositories = {
  shipments: {
    async listMine() {
      return [
        {
          id: 's1',
          reference: 'VL-4821',
          from: montreal,
          to: paris,
          description: 'Livres et carnets',
          weightKg: 2,
          status: 'in_transit',
          price: { amountMinor: 3500, currency: 'CAD' },
        },
        {
          id: 's2',
          reference: 'VL-5307',
          from: montreal,
          to: casablanca,
          description: 'Vêtements pour enfant',
          weightKg: 1.5,
          status: 'requested',
        },
      ];
    },
  },
  trips: {
    async listMine() {
      return [
        {
          id: 't1',
          from: montreal,
          to: paris,
          departureDate: '2026-11-14',
          flightNumber: 'AC870',
          capacityKg: 5,
        },
      ];
    },
    async search() {
      return this.listMine();
    },
  },
  messages: {
    async listConversations() {
      return [
        {
          id: 'c1',
          participantName: 'Samira B.',
          lastMessage: 'Parfait, rendez-vous à 18 h devant la gare.',
          updatedAt: '2026-10-11T18:20:00-04:00',
          unread: 2,
        },
      ];
    },
  },
  profile: {
    async getMe() {
      return { id: 'u1', displayName: 'Utilisateur Volis', identityVerified: false };
    },
  },
};
