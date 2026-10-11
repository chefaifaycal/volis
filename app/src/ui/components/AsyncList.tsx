import { ActivityIndicator, Text } from 'react-native';

import { useTheme } from '@/theme';
import type { AsyncState, ListItemVM } from '@/ui/viewmodels';

import { Card } from './Card';
import type { IconName } from './Icon';

export function AsyncList({ state, icon, empty }: { state: AsyncState<readonly ListItemVM[]>; icon: IconName; empty: string }) {
  const t = useTheme();
  if (state.kind === 'loading') return <ActivityIndicator color={t.colors.primary} />;
  if (state.kind === 'error') return <Text style={[t.typography.body, { color: t.colors.errorText }]}>{state.message}</Text>;
  if (state.data.length === 0) return <Text style={[t.typography.body, { color: t.colors.textMuted }]}>{empty}</Text>;
  return (
    <>
      {state.data.map((item) => (
        <Card key={item.id} icon={icon} title={item.title} subtitle={item.subtitle} meta={item.meta} />
      ))}
    </>
  );
}
