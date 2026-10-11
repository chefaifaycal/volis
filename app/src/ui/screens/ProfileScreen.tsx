import { ActivityIndicator, Text } from 'react-native';

import { useTheme } from '@/theme';
import { Card } from '@/ui/components/Card';
import { Screen } from '@/ui/components/Screen';
import { useProfileViewModel } from '@/ui/viewmodels';

export function ProfileScreen() {
  const t = useTheme();
  const state = useProfileViewModel();
  return (
    <Screen title="Profil">
      {state.kind === 'loading' ? <ActivityIndicator color={t.colors.primary} /> : null}
      {state.kind === 'error' ? <Text style={{ color: t.colors.errorText }}>{state.message}</Text> : null}
      {state.kind === 'ready' ? (
        <>
          <Card icon="user" title={state.data.displayName} meta={state.data.identityLabel} />
          <Card icon="id-card" title="Vérifier mon identité" subtitle="Via Stripe Identity (hébergé)" />
          <Card icon="wallet" title="Portefeuille et versements" subtitle="Via Stripe Connect (hébergé)" />
          <Card icon="sliders" title="Réglages" />
        </>
      ) : null}
    </Screen>
  );
}
