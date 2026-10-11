import { inMemoryRepositories } from './fakes/inMemory';
import type { Repositories } from './repositories/types';

export type * from './repositories/types';
export { env, isBackendConfigured } from './config/env';

// TODO : remplacer par les implémentations Supabase (src/data/api) quand le projet sera créé.
export const repositories: Repositories = inMemoryRepositories;
