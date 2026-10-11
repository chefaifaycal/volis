import type { Conversation, Shipment, Trip, UserProfile } from '@/domain';

// Contrats des repositories : point unique d'accès au réseau, au cache et au stockage sécurisé.
// L'UI ne doit jamais appeler le réseau directement (cahier technique, partie B §2.2).
export interface ShipmentsRepository {
  listMine(): Promise<readonly Shipment[]>;
}

export interface TripsRepository {
  listMine(): Promise<readonly Trip[]>;
  search(params: { fromCity?: string; toCity?: string }): Promise<readonly Trip[]>;
}

export interface MessagesRepository {
  listConversations(): Promise<readonly Conversation[]>;
}

export interface ProfileRepository {
  getMe(): Promise<UserProfile>;
}

export interface Repositories {
  shipments: ShipmentsRepository;
  trips: TripsRepository;
  messages: MessagesRepository;
  profile: ProfileRepository;
}
