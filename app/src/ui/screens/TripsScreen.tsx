import { AsyncList } from '@/ui/components/AsyncList';
import { Screen } from '@/ui/components/Screen';
import { useTripsViewModel } from '@/ui/viewmodels';

export function TripsScreen() {
  const state = useTripsViewModel();
  return (
    <Screen title="Mes voyages">
      <AsyncList state={state} icon="plane" empty="Aucun voyage publié." />
    </Screen>
  );
}
