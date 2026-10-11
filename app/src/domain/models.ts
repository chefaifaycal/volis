import type { BookingStatus } from './booking';
import type { Money } from './money';

export interface Place {
  readonly city: string;
  readonly countryCode: string;
  readonly airportCode?: string;
}

export interface Shipment {
  readonly id: string;
  readonly reference: string;
  readonly from: Place;
  readonly to: Place;
  readonly description: string;
  readonly weightKg: number;
  readonly status: BookingStatus;
  readonly price?: Money;
}

export interface Trip {
  readonly id: string;
  readonly from: Place;
  readonly to: Place;
  readonly departureDate: string; // ISO 8601
  readonly flightNumber?: string;
  readonly capacityKg: number;
}

export interface Conversation {
  readonly id: string;
  readonly participantName: string;
  readonly lastMessage: string;
  readonly updatedAt: string; // ISO 8601
  readonly unread: number;
}

export interface UserProfile {
  readonly id: string;
  readonly displayName: string;
  readonly identityVerified: boolean;
  readonly rating?: number;
}
