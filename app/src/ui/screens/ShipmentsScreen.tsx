import { AsyncList } from '@/ui/components/AsyncList';
import { Screen } from '@/ui/components/Screen';
import { useShipmentsViewModel } from '@/ui/viewmodels';

export function ShipmentsScreen() {
  const state = useShipmentsViewModel();
  return (
    <Screen title="Mes envois">
      <AsyncList state={state} icon="package" empty="Aucun envoi pour le moment." />
    </Screen>
  );
}
