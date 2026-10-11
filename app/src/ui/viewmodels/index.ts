import { repositories } from '@/data';
import { bookingStatusLabel, formatMoney, type Shipment, type Trip } from '@/domain';

import { useAsyncState } from './useAsyncState';

export type { AsyncState } from './useAsyncState';

export interface ListItemVM {
  readonly id: string;
  readonly title: string;
  readonly subtitle: string;
  readonly meta?: string;
}

const route = (s: Shipment | Trip) =>
  `${s.from.airportCode ?? s.from.city} → ${s.to.airportCode ?? s.to.city}`;

export function useShipmentsViewModel() {
  return useAsyncState<readonly ListItemVM[]>(async () =>
    (await repositories.shipments.listMine()).map((s) => ({
      id: s.id,
      title: `${s.reference} · ${route(s)}`,
      subtitle: `${s.description} · ${s.weightKg} kg`,
      meta: [bookingStatusLabel[s.status], s.price ? formatMoney(s.price) : undefined]
        .filter(Boolean)
        .join(' · '),
    })),
  );
}

export function useTripsViewModel() {
  return useAsyncState<readonly ListItemVM[]>(async () =>
    (await repositories.trips.listMine()).map((t) => ({
      id: t.id,
      title: route(t),
      subtitle: `${t.departureDate}${t.flightNumber ? ` · vol ${t.flightNumber}` : ''}`,
      meta: `${t.capacityKg} kg disponibles`,
    })),
  );
}

export function useMessagesViewModel() {
  return useAsyncState<readonly ListItemVM[]>(async () =>
    (await repositories.messages.listConversations()).map((c) => ({
      id: c.id,
      title: c.participantName,
      subtitle: c.lastMessage,
      meta: c.unread > 0 ? `${c.unread} non lu(s)` : undefined,
    })),
  );
}

export function useProfileViewModel() {
  return useAsyncState(async () => {
    const me = await repositories.profile.getMe();
    return {
      displayName: me.displayName,
      identityLabel: me.identityVerified ? 'Identité vérifiée' : 'Identité non vérifiée',
      identityVerified: me.identityVerified,
    } as const;
  });
}
