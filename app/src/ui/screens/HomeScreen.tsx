import { Text, View } from 'react-native';

import { isBackendConfigured } from '@/data';
import { useTheme } from '@/theme';
import { Card } from '@/ui/components/Card';
import { Icon } from '@/ui/components/Icon';
import { Screen } from '@/ui/components/Screen';

export function HomeScreen() {
  const t = useTheme();
  return (
    <Screen title="Bonjour 👋" subtitle="Envoyez un colis avec un voyageur vérifié, ou rentabilisez vos kilos libres.">
      <View
        style={{
          flexDirection: 'row',
          gap: t.space['1'],
          padding: t.space['1.5'],
          borderRadius: t.radii.md,
          backgroundColor: t.colors.mint,
        }}>
        <Icon name="shield" size={20} color={t.colors.primaryPressed} />
        <Text style={[t.typography.caption, { color: t.colors.text, flex: 1 }]}>
          Votre argent est protégé : il reste en séquestre jusqu’à la remise.
        </Text>
      </View>
      <Card icon="package" title="Envoyer un colis" subtitle="Trouvez un voyageur sur votre trajet" />
      <Card icon="plane" title="Publier un voyage" subtitle="Indiquez vos dates et la place disponible" />
      {!isBackendConfigured ? (
        <Text style={[t.typography.micro, { color: t.colors.textMuted }]}>
          Mode démo : données fictives (backend non configuré, voir .env.example).
        </Text>
      ) : null}
    </Screen>
  );
}
