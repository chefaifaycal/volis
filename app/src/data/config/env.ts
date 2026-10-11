// Seules les variables EXPO_PUBLIC_* sont incluses dans le bundle : elles sont donc PUBLIQUES.
// Ne jamais y mettre de secret (clé service_role Supabase, clé secrète Stripe, etc.).
export const env = {
  supabaseUrl: process.env.EXPO_PUBLIC_SUPABASE_URL ?? '',
  supabaseAnonKey: process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY ?? '',
  stripePublishableKey: process.env.EXPO_PUBLIC_STRIPE_PUBLISHABLE_KEY ?? '',
} as const;

export const isBackendConfigured = env.supabaseUrl !== '' && env.supabaseAnonKey !== '';
